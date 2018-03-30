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

import json
import pytest
import requests
import time
from tests.common.custom_cluster_test_suite import CustomClusterTestSuite
from tests.common.impala_cluster import ImpalaCluster
from tests.common.skip import SkipIf, SkipIfBuildType
from tests.verifiers.mem_usage_verifier import MemUsageVerifier

@SkipIf.not_krpc
class TestKrpcMetrics(CustomClusterTestSuite):
  """Test for KRPC metrics that require special arguments during cluster startup."""
  RPCZ_URL = 'http://localhost:25000/rpcz?json'
  METRICS_URL = 'http://localhost:25000/metrics?json'
  TEST_QUERY = 'select count(*) from tpch_parquet.lineitem l1 \
      join tpch_parquet.lineitem l2 where l1.l_orderkey = l2.l_orderkey;'

  @classmethod
  def get_workload(self):
    return 'functional-query'

  @classmethod
  def setup_class(cls):
    if cls.exploration_strategy() != 'exhaustive':
      pytest.skip('runs only in exhaustive')
    super(TestKrpcMetrics, cls).setup_class()

  def get_debug_page(self, page_url):
    """Returns the content of the debug page 'page_url' as json."""
    response = requests.get(page_url)
    assert response.status_code == requests.codes.ok
    return json.loads(response.text)

  def get_service_json(self, name):
    rpcz = self.get_debug_page(self.RPCZ_URL)
    assert len(rpcz['services']) > 0
    for s in rpcz['services']:
      if s['service_name'] == name:
        return s
    assert False, 'Could not find metrics for service %s' % name

  @pytest.mark.execute_serially
  @CustomClusterTestSuite.with_args('-datastream_service_queue_mem_limit=1B \
                                     -datastream_service_num_svc_threads=1')
  def test_krpc_queue_overflow_rpcz(self, vector):
    """Test that rejected RPCs show up on the /rpcz debug web page."""
    def get_rpc_overflows():
      s = self.get_service_json('impala.DataStreamService')
      return int(s['rpcs_queue_overflow'])

    before = get_rpc_overflows()
    assert before == 0
    self.client.execute(self.TEST_QUERY)
    after = get_rpc_overflows()

    assert before < after

  def test_krpc_histograms(self, vector):
    """Test that the KRPC histograms on /rpcz are structured json."""
    self.client.execute(self.TEST_QUERY)
    s = self.get_service_json('impala.DataStreamService')
    def get_method_metrics(name):
      for m in s['rpc_method_metrics']:
        if m['method_name'] == name:
          return m
      assert False, 'Could not find metrics for method %s' % name

    for method in ['EndDataStream', 'TransmitData']:
      method_metrics = get_method_metrics(method)
      for histogram in ['handler_latency', 'handler_latency']:
        assert int(method_metrics[histogram]['count']) > 0

  def iter_metrics(self, group = None):
    group = group or self.get_debug_page(self.METRICS_URL)['metric_group']
    for m in group['metrics']:
      yield m
    for c in group['child_groups']:
      for m in self.iter_metrics(c):
        yield m

  def get_metric(self, name):
    """Finds the metric with name 'name' and returns its value as an int."""
    for m in self.iter_metrics():
      if m['name'] == name:
        return m
    assert False, "Could not find metric: %s" % name

  def get_counter(self, name):
    """Returns the value of the COUNTER metric 'name' as an int."""
    m = self.get_metric(name)
    assert m['kind'] == 'COUNTER', "Metric is of wrong type: %s" % m['kind']
    return int(m['value'])

  def get_gauge(self, name):
    """Returns the value of the GAUGE metric 'name' as an int."""
    m = self.get_metric(name)
    assert m['kind'] == 'GAUGE', "Metric is of wrong type: %s" % m['kind']
    return int(m['value'])

  def get_histogram_metric(self, name):
    """Returns the HISTOGRAM metric 'name' as a dict."""
    m = self.get_metric(name)
    assert m['kind'] == 'HISTOGRAM', "Metric is of wrong type: %s" % m['kind']
    return m

  @pytest.mark.execute_serially
  @CustomClusterTestSuite.with_args('-datastream_service_queue_mem_limit=1B \
                                     -datastream_service_num_svc_threads=1')
  def test_krpc_queue_overflow_metrics(self, vector):
    """Test that rejected RPCs show up on the /metrics debug web page.
    """
    metric_name = 'rpc.impala.DataStreamService.rpcs_queue_overflow'
    before = self.get_counter(metric_name)
    assert before == 0

    self.client.execute(self.TEST_QUERY)
    after = self.get_counter(metric_name)
    assert before < after

  @pytest.mark.execute_serially
  def test_krpc_service_metrics(self, vector):
    """Test that KRPC metrics show up on the /metrics debug web page.
    """
    self.client.execute(self.TEST_QUERY)
    assert self.get_gauge('mem-tracker.DataStreamService.current_usage_bytes') >= 0
    assert self.get_gauge('mem-tracker.DataStreamService.peak_usage_bytes') > 0

    histogram_names = ['rpc.impala.DataStreamService.EndDataStream.handler_latency',
                       'rpc.impala.DataStreamService.EndDataStream.incoming_payload_size',
                       'rpc.impala.DataStreamService.TransmitData.handler_latency',
                       'rpc.impala.DataStreamService.TransmitData.incoming_payload_size',
                       'rpc.impala.DataStreamService.incoming_queue_time']

    for name in histogram_names:
      m = self.get_histogram_metric(name)
      assert int(m['count']) > 0
      assert int(m['99.9th %-ile']) >= int(m['25th %-ile']) >= 0
      assert m['units'] in ['BYTES', 'TIME_US']


