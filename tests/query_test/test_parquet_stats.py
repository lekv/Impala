# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

import os
import pytest
import random
import shlex
from subprocess import check_call

from tests.common.test_vector import ImpalaTestDimension
from tests.common.impala_test_suite import ImpalaTestSuite
from tests.util.filesystem_utils import get_fs_path
from tests.common.test_result_verifier import (
  verify_query_result_is_equal,
  create_query_result)

MT_DOP_VALUES = [0, 1, 2, 8]

class TestParquetStats(ImpalaTestSuite):
  """
  This suite tests runtime optimizations based on Parquet statistics.
  """

  @classmethod
  def get_workload(cls):
    return 'functional-query'

  @classmethod
  def add_test_dimensions(cls):
    super(TestParquetStats, cls).add_test_dimensions()
    # TODO: re-enable
    # cls.ImpalaTestMatrix.add_dimension(ImpalaTestDimension('mt_dop', *MT_DOP_VALUES))
    cls.ImpalaTestMatrix.add_constraint(
        lambda v: v.get_value('table_format').file_format == 'parquet')

  def test_parquet_stats(self, vector, unique_database):
    # The test makes assumptions about the number of row groups that are processed and
    # skipped inside a fragment, so we ensure that the tests run in a single fragment.
    vector.get_value('exec_option')['num_nodes'] = 1
    self.run_test_case('QueryTest/parquet-stats', vector, use_db=unique_database)

  def test_deprecated_stats(self, vector, unique_database):
    """Test that reading parquet files with statistics with deprecated 'min'/'max' fields
    works correctly. The statistics will be used for known-good types (boolean, integral,
    float) and will be ignored for all other types (string, decimal, timestamp)."""
    table_name = 'deprecated_stats'
    # We use CTAS instead of "create table like" to convert the partition columns into
    # normal table columns.
    self.client.execute('create table %s.%s stored as parquet as select * from '
                        'functional.alltypessmall limit 0' %
                        (unique_database, table_name))
    table_location = get_fs_path('/test-warehouse/%s.db/%s' %
                                 (unique_database, table_name))
    local_file = os.path.join(os.environ['IMPALA_HOME'],
                              'testdata/data/deprecated_statistics.parquet')
    assert os.path.isfile(local_file)
    check_call(['hdfs', 'dfs', '-copyFromLocal', local_file, table_location])
    self.client.execute('invalidate metadata %s.%s' % (unique_database, table_name))
    # The test makes assumptions about the number of row groups that are processed and
    # skipped inside a fragment, so we ensure that the tests run in a single fragment.
    vector.get_value('exec_option')['num_nodes'] = 1
    self.run_test_case('QueryTest/parquet-deprecated-stats', vector, unique_database)

  def test_page_stats_smoke(self, vector):
    """Make sure that these don't crash."""
    queries = [
      """SELECT c_custkey, c_orders.o_orderkey, count(*) FROM
      tpch_nested_parquet.customer, customer.c_orders c_orders, c_orders.o_lineitems GROUP
      BY c_custkey, c_orders.o_orderkey LIMIT 5;""",
      # Tests selecting from bool columns.
      """select * from functional_parquet.alltypessmall;""",
      # Tests skipping bool columns
      """select count(*) from default.parquet_ibs where bool_col = false and id <
      500000;""",
      """select id, ar.item from i5185.s, s.a ar where id = 131073 limit 8;""",
      """select a.tinyint_col, b.id, a.string_col
      from functional_parquet.alltypesagg a cross join functional_parquet.alltypessmall b
      where a.tinyint_col = b.id
      and a.month=1
      and a.day=1
      and b.bool_col = false;""",
      """select a.tinyint_col, b.id, a.string_col
      from functional_parquet.alltypesagg a cross join functional_parquet.alltypessmall b
      where a.tinyint_col = b.id
      and a.month=1
      and a.day=1
      and a.tinyint_col + b.tinyint_col < 5
      and a.string_col > '88'
      and b.bool_col = false;"""
    ]
    map(self.execute_query, queries)

  def test_compare_queries(self, vector, unique_database):
    reference_table = "tpch.lineitem"
    test_table = "%s.lineitem" % unique_database
    test_table = "default.l"

    # Create test table
    # self.client.execute('create table %s sort by (l_suppkey, l_orderkey) stored as '
    #                     'parquet as select * from tpch.lineitem' % test_table)

    # Hardcoded parameters that triggered corner cases during development.
    params = [
      ('=', 5000, '<', 10000),
      ('=', 7993, '=', 6242),
    ]
    query_tmpl = """select * from {0} where l_suppkey {1} {2} and l_orderkey {3} {4} order
        by l_orderkey, l_linenumber limit 100;"""

    random.seed(123)
    # generate random queries
    pred = lambda: random.choice("<=>")
    for i in xrange(200):
      params.append(
          [pred(), random.randint(1, 10000), pred(), random.randint(1, 6000000)])

    for p in params:
      expected = create_query_result(
          self.execute_query(query_tmpl.format(reference_table, *p)))
      actual = create_query_result(self.execute_query(query_tmpl.format(test_table, *p)))
      verify_query_result_is_equal(actual, expected)
