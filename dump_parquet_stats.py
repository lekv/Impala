#!/usr/bin/env impala-python

from decimal import Decimal
import sys
import time

from parquet.ttypes import Type
from tests.util.get_parquet_metadata import get_parquet_metadata, decode_stats_value

def process_file(parquet_file):
  file_meta_data = get_parquet_metadata(parquet_file)
  schemas = file_meta_data.schema[1:]
  assert len(file_meta_data.row_groups) == 1
  row_group = file_meta_data.row_groups[0]

  for column, schema in zip(row_group.columns, schemas):
    column_meta_data = column.meta_data
    stats = column_meta_data.statistics


    if not stats:
      continue

    if stats.min_value:
      min_value = decode_stats_value(schema, stats.min_value)

    if stats.max_value:
      max_value = decode_stats_value(schema, stats.max_value)

    codec = {
      0: "UNCOMPRESSED",
      1: "SNAPPY",
      2: "GZIP",
      3: "LZO",
    }

    codec_name = codec[column_meta_data.codec]

    # print "%s %s %s %s" % (schema.name, codec_name, str(min_value), str(max_value))
    print "%s %s %s" % (schema.name, str(min_value), str(max_value))
    # print "min: %s" % str(min_value)
    # print "max: %s" % str(max_value)


if __name__ == "__main__":
  process_file(sys.argv[1])
