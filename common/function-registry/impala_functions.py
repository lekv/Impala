#!/usr/bin/env python
# Copyright 2012 Cloudera Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# This is a list of all the functions that are not auto-generated.
# It contains all the meta data that describes the function.
templated_type_symbol_map = {
  'bool'      : 'b',
  'int8_t'    : 'a',
  'int16_t'   : 's',
  'int32_t'   : 'i',
  'int64_t'   : 'l',
  'float'     : 'f',
  'double'    : 'd',
  'string'    : 'NS_11StringValueE',
  'timestamp' : 'NS_14TimestampValueE'
}

# Generates the BE symbol for the Compute Function class_name::fn_name<templated_type>.
# Does not handle varargs.
# TODO: this is a stopgap. ComputeFunctions are being removed and we can use the
# symbol lookup code in the BE.
def symbol(class_name, fn_name, templated_type = None):
  sym = '_ZN6impala'
  sym += str(len(class_name)) + class_name
  sym += str(len(fn_name)) + fn_name
  if templated_type == None:
    sym += 'EPNS_4ExprEPNS_8TupleRowE'
  else:
    sym += 'I'
    sym += templated_type_symbol_map[templated_type]
    sym += 'EEPvPNS_4ExprEPNS_8TupleRowE'
  return sym

# The format is:
#   [sql aliases], <return_type>, [<args>], <backend symbol>,
# With an optional
#   <prepare symbol>, <close symbol>
#
# 'sql aliases' are the function names that can be used from sql. There must be
# at least one per function.
#
# The symbol can be empty for functions that are not yet implemented.
functions = [
  # String builtin functions
  [['substr', 'substring'], 'STRING', ['STRING', 'INT'],
      symbol('StringFunctions', 'Substring', 'int32_t')],
  [['substr', 'substring'], 'STRING', ['STRING', 'BIGINT'],
      symbol('StringFunctions', 'Substring', 'int64_t')],
  [['substr', 'substring'], 'STRING', ['STRING', 'INT', 'INT'],
      symbol('StringFunctions', 'Substring', 'int32_t')],
  [['substr', 'substring'], 'STRING', ['STRING', 'BIGINT', 'BIGINT'],
      symbol('StringFunctions', 'Substring', 'int64_t')],
# left and right are key words, leave them out for now.
  [['strleft'], 'STRING', ['STRING', 'INT'],
      symbol('StringFunctions', 'Left', 'int32_t')],
  [['strleft'], 'STRING', ['STRING', 'BIGINT'],
      symbol('StringFunctions', 'Left', 'int64_t')],
  [['strright'], 'STRING', ['STRING', 'INT'],
      symbol('StringFunctions', 'Right', 'int32_t')],
  [['strright'], 'STRING', ['STRING', 'BIGINT'],
      symbol('StringFunctions', 'Right', 'int64_t')],
  [['space'], 'STRING', ['INT'], symbol('StringFunctions', 'Space', 'int32_t')],
  [['space'], 'STRING', ['BIGINT'], symbol('StringFunctions', 'Space', 'int64_t')],
  [['repeat'], 'STRING', ['STRING', 'INT'],
      symbol('StringFunctions', 'Repeat', 'int32_t')],
  [['repeat'], 'STRING', ['STRING', 'BIGINT'],
      symbol('StringFunctions', 'Repeat', 'int64_t')],
  [['lpad'], 'STRING', ['STRING', 'INT', 'STRING'],
      symbol('StringFunctions', 'Lpad', 'int32_t')],
  [['lpad'], 'STRING', ['STRING', 'BIGINT', 'STRING'],
      symbol('StringFunctions', 'Lpad', 'int64_t')],
  [['rpad'], 'STRING', ['STRING', 'INT', 'STRING'],
      symbol('StringFunctions', 'Rpad', 'int32_t')],
  [['rpad'], 'STRING', ['STRING', 'BIGINT', 'STRING'],
      symbol('StringFunctions', 'Rpad', 'int64_t')],
  [['length'], 'INT', ['STRING'], symbol('StringFunctions', 'Length')],
  [['char_length'], 'INT', ['STRING'], symbol('StringFunctions', 'Length')],
  [['character_length'], 'INT', ['STRING'], symbol('StringFunctions', 'Length')],
  [['lower', 'lcase'], 'STRING', ['STRING'], symbol('StringFunctions', 'Lower')],
  [['upper', 'ucase'], 'STRING', ['STRING'], symbol('StringFunctions', 'Upper')],
  [['initcap'], 'STRING', ['STRING'], symbol('StringFunctions', 'InitCap')],
  [['reverse'], 'STRING', ['STRING'], symbol('StringFunctions', 'Reverse')],
  [['translate'], 'STRING', ['STRING', 'STRING', 'STRING'],
      symbol('StringFunctions', 'Translate')],
  [['trim'], 'STRING', ['STRING'], symbol('StringFunctions', 'Trim')],
  [['ltrim'], 'STRING', ['STRING'], symbol('StringFunctions', 'Ltrim')],
  [['rtrim'], 'STRING', ['STRING'], symbol('StringFunctions', 'Rtrim')],
  [['ascii'], 'INT', ['STRING'], symbol('StringFunctions', 'Ascii')],
  [['instr'], 'INT', ['STRING', 'STRING'], symbol('StringFunctions', 'Instr')],
  [['locate'], 'INT', ['STRING', 'STRING'], symbol('StringFunctions', 'Locate')],
  [['locate'], 'INT', ['STRING', 'STRING', 'INT'],
      symbol('StringFunctions', 'LocatePos', 'int32_t')],
  [['locate'], 'INT', ['STRING', 'STRING', 'BIGINT'],
      symbol('StringFunctions', 'LocatePos', 'int64_t')],
  [['regexp_extract'], 'STRING', ['STRING', 'STRING', 'INT'],
      symbol('StringFunctions', 'RegexpExtract', 'int32_t')],
  [['regexp_extract'], 'STRING', ['STRING', 'STRING', 'BIGINT'],
      symbol('StringFunctions', 'RegexpExtract', 'int64_t')],
  [['regexp_replace'], 'STRING', ['STRING', 'STRING', 'STRING'],
      symbol('StringFunctions', 'RegexpReplace')],
  [['concat'], 'STRING', ['STRING', '...'], symbol('StringFunctions', 'Concat')],
  [['concat_ws'], 'STRING', ['STRING', 'STRING', '...'],
      symbol('StringFunctions', 'ConcatWs')],
  [['find_in_set'], 'INT', ['STRING', 'STRING'], symbol('StringFunctions', 'FindInSet')],
  [['parse_url'], 'STRING', ['STRING', 'STRING'], symbol('StringFunctions', 'ParseUrl')],
  [['parse_url'], 'STRING', ['STRING', 'STRING', 'STRING'],
      symbol('StringFunctions', 'ParseUrlKey')],

  # Utility functions
  [['current_database'], 'STRING', [], symbol('UtilityFunctions', 'CurrentDatabase')],
  [['user'], 'STRING', [], symbol('UtilityFunctions', 'User')],
  [['sleep'], 'BOOLEAN', ['INT'], symbol('UtilityFunctions', 'Sleep')],
  [['pid'], 'INT', [], symbol('UtilityFunctions', 'Pid')],
  [['version'], 'STRING', [], symbol('UtilityFunctions', 'Version')],

  [['fnv_hash'], 'BIGINT', ['TINYINT'],
      '_ZN6impala16UtilityFunctions7FnvHashILi1EEEPvPNS_4ExprEPNS_8TupleRowE'],
  [['fnv_hash'], 'BIGINT', ['SMALLINT'],
      '_ZN6impala16UtilityFunctions7FnvHashILi2EEEPvPNS_4ExprEPNS_8TupleRowE'],
  [['fnv_hash'], 'BIGINT', ['INT'],
      '_ZN6impala16UtilityFunctions7FnvHashILi4EEEPvPNS_4ExprEPNS_8TupleRowE'],
  [['fnv_hash'], 'BIGINT', ['BIGINT'],
      '_ZN6impala16UtilityFunctions7FnvHashILi8EEEPvPNS_4ExprEPNS_8TupleRowE'],
  [['fnv_hash'], 'BIGINT', ['FLOAT'],
      '_ZN6impala16UtilityFunctions7FnvHashILi4EEEPvPNS_4ExprEPNS_8TupleRowE'],
  [['fnv_hash'], 'BIGINT', ['DOUBLE'],
      '_ZN6impala16UtilityFunctions7FnvHashILi8EEEPvPNS_4ExprEPNS_8TupleRowE'],
  [['fnv_hash'], 'BIGINT', ['TIMESTAMP'],
      '_ZN6impala16UtilityFunctions7FnvHashILi12EEEPvPNS_4ExprEPNS_8TupleRowE'],
  [['fnv_hash'], 'BIGINT', ['STRING'],
      '_ZN6impala16UtilityFunctions13FnvHashStringEPNS_4ExprEPNS_8TupleRowE'],
  [['fnv_hash'], 'BIGINT', ['DECIMAL'], symbol('UtilityFunctions', 'FnvHashDecimal')],

  # Timestamp Functions

  [['from_utc_timestamp'], 'TIMESTAMP', ['TIMESTAMP', 'STRING'],
          symbol('TimestampFunctions', 'FromUtc')],
  [['to_utc_timestamp'], 'TIMESTAMP', ['TIMESTAMP', 'STRING'],
          symbol('TimestampFunctions', 'ToUtc')],

  # Date and time add/sub functions.
  # TODO: there must be a better way to deal with this symbols.



  # Conditional Functions
  [['if'], 'BOOLEAN', ['BOOLEAN', 'BOOLEAN', 'BOOLEAN'],
      symbol('ConditionalFunctions', 'IfFn')],
  [['if'], 'TINYINT', ['BOOLEAN', 'TINYINT', 'TINYINT'],
      symbol('ConditionalFunctions', 'IfFn')],
  [['if'], 'SMALLINT', ['BOOLEAN', 'SMALLINT', 'SMALLINT'],
      symbol('ConditionalFunctions', 'IfFn')],
  [['if'], 'INT', ['BOOLEAN', 'INT', 'INT'],
      symbol('ConditionalFunctions', 'IfFn')],
  [['if'], 'BIGINT', ['BOOLEAN', 'BIGINT', 'BIGINT'],
      symbol('ConditionalFunctions', 'IfFn')],
  [['if'], 'FLOAT', ['BOOLEAN', 'FLOAT', 'FLOAT'],
      symbol('ConditionalFunctions', 'IfFn')],
  [['if'], 'DOUBLE', ['BOOLEAN', 'DOUBLE', 'DOUBLE'],
      symbol('ConditionalFunctions', 'IfFn')],
  [['if'], 'STRING', ['BOOLEAN', 'STRING', 'STRING'],
      symbol('ConditionalFunctions', 'IfFn')],
  [['if'], 'TIMESTAMP', ['BOOLEAN', 'TIMESTAMP', 'TIMESTAMP'],
      symbol('ConditionalFunctions', 'IfFn')],
  [['if'], 'DECIMAL', ['BOOLEAN', 'DECIMAL', 'DECIMAL'],
      symbol('ConditionalFunctions', 'IfFn')],

  [['nullif'], 'BOOLEAN', ['BOOLEAN', 'BOOLEAN'],
      symbol('ConditionalFunctions', 'NullIf', 'bool')],
  [['nullif'], 'TINYINT', ['TINYINT', 'TINYINT'],
      symbol('ConditionalFunctions', 'NullIf', 'int8_t')],
  [['nullif'], 'SMALLINT', ['SMALLINT', 'SMALLINT'],
      symbol('ConditionalFunctions', 'NullIf', 'int16_t')],
  [['nullif'], 'INT', ['INT', 'INT'],
      symbol('ConditionalFunctions', 'NullIf', 'int32_t')],
  [['nullif'], 'BIGINT', ['BIGINT', 'BIGINT'],
      symbol('ConditionalFunctions', 'NullIf', 'int64_t')],
  [['nullif'], 'FLOAT', ['FLOAT', 'FLOAT'],
      symbol('ConditionalFunctions', 'NullIf', 'float')],
  [['nullif'], 'DOUBLE', ['DOUBLE', 'DOUBLE'],
      symbol('ConditionalFunctions', 'NullIf', 'double')],
  [['nullif'], 'STRING', ['STRING', 'STRING'],
      symbol('ConditionalFunctions', 'NullIf', 'string')],
  [['nullif'], 'TIMESTAMP', ['TIMESTAMP', 'TIMESTAMP'],
      symbol('ConditionalFunctions', 'NullIf', 'timestamp')],
  [['nullif'], 'DECIMAL', ['DECIMAL', 'DECIMAL'],
      symbol('ConditionalFunctions', 'NullIfDecimal')],

  [['zeroifnull'], 'TINYINT', ['TINYINT'],
      symbol('ConditionalFunctions', 'ZeroIfNull', 'int8_t')],
  [['zeroifnull'], 'SMALLINT', ['SMALLINT'],
      symbol('ConditionalFunctions', 'ZeroIfNull', 'int16_t')],
  [['zeroifnull'], 'INT', ['INT'],
      symbol('ConditionalFunctions', 'ZeroIfNull', 'int32_t')],
  [['zeroifnull'], 'BIGINT', ['BIGINT'],
      symbol('ConditionalFunctions', 'ZeroIfNull', 'int64_t')],
  [['zeroifnull'], 'FLOAT', ['FLOAT'],
      symbol('ConditionalFunctions', 'ZeroIfNull', 'float')],
  [['zeroifnull'], 'DOUBLE', ['DOUBLE'],
      symbol('ConditionalFunctions', 'ZeroIfNull', 'double')],
  [['zeroifnull'], 'DECIMAL', ['DECIMAL'],
      symbol('ConditionalFunctions', 'ZeroIfNullDecimal')],

  [['nullifzero'], 'TINYINT', ['TINYINT'],
      symbol('ConditionalFunctions', 'NullIfZero', 'int8_t')],
  [['nullifzero'], 'SMALLINT', ['SMALLINT'],
      symbol('ConditionalFunctions', 'NullIfZero', 'int16_t')],
  [['nullifzero'], 'INT', ['INT'],
      symbol('ConditionalFunctions', 'NullIfZero', 'int32_t')],
  [['nullifzero'], 'BIGINT', ['BIGINT'],
      symbol('ConditionalFunctions', 'NullIfZero', 'int64_t')],
  [['nullifzero'], 'FLOAT', ['FLOAT'],
      symbol('ConditionalFunctions', 'NullIfZero', 'float')],
  [['nullifzero'], 'DOUBLE', ['DOUBLE'],
      symbol('ConditionalFunctions', 'NullIfZero', 'double')],
  [['nullifzero'], 'DECIMAL', ['DECIMAL'],
      symbol('ConditionalFunctions', 'NullIfZeroDecimal')],

  [['isnull', 'ifnull', 'nvl'], 'BOOLEAN', ['BOOLEAN', 'BOOLEAN'],
      symbol('ConditionalFunctions', 'IsNull')],
  [['isnull', 'ifnull', 'nvl'], 'TINYINT', ['TINYINT', 'TINYINT'],
      symbol('ConditionalFunctions', 'IsNull')],
  [['isnull', 'ifnull', 'nvl'], 'SMALLINT', ['SMALLINT', 'SMALLINT'],
      symbol('ConditionalFunctions', 'IsNull')],
  [['isnull', 'ifnull', 'nvl'], 'INT', ['INT', 'INT'],
      symbol('ConditionalFunctions', 'IsNull')],
  [['isnull', 'ifnull', 'nvl'], 'BIGINT', ['BIGINT', 'BIGINT'],
      symbol('ConditionalFunctions', 'IsNull')],
  [['isnull', 'ifnull', 'nvl'], 'FLOAT', ['FLOAT', 'FLOAT'],
      symbol('ConditionalFunctions', 'IsNull')],
  [['isnull', 'ifnull', 'nvl'], 'DOUBLE', ['DOUBLE', 'DOUBLE'],
      symbol('ConditionalFunctions', 'IsNull')],
  [['isnull', 'ifnull', 'nvl'], 'STRING', ['STRING', 'STRING'],
      symbol('ConditionalFunctions', 'IsNull')],
  [['isnull', 'ifnull', 'nvl'], 'TIMESTAMP', ['TIMESTAMP', 'TIMESTAMP'],
      symbol('ConditionalFunctions', 'IsNull')],
  [['isnull', 'ifnull', 'nvl'], 'DECIMAL', ['DECIMAL', 'DECIMAL'],
      symbol('ConditionalFunctions', 'IsNull')],

  [['coalesce'], 'BOOLEAN', ['BOOLEAN', '...'],
   symbol('ConditionalFunctions', 'Coalesce')],
  [['coalesce'], 'TINYINT', ['TINYINT', '...'],
   symbol('ConditionalFunctions', 'Coalesce')],
  [['coalesce'], 'SMALLINT', ['SMALLINT', '...'],
   symbol('ConditionalFunctions', 'Coalesce')],
  [['coalesce'], 'INT', ['INT', '...'], symbol('ConditionalFunctions', 'Coalesce')],
  [['coalesce'], 'BIGINT', ['BIGINT', '...'], symbol('ConditionalFunctions', 'Coalesce')],
  [['coalesce'], 'FLOAT', ['FLOAT', '...'], symbol('ConditionalFunctions', 'Coalesce')],
  [['coalesce'], 'DOUBLE', ['DOUBLE', '...'], symbol('ConditionalFunctions', 'Coalesce')],
  [['coalesce'], 'STRING', ['STRING', '...'], symbol('ConditionalFunctions', 'Coalesce')],
  [['coalesce'], 'TIMESTAMP', ['TIMESTAMP', '...'],
   symbol('ConditionalFunctions', 'Coalesce')],
  [['coalesce'], 'DECIMAL', ['DECIMAL', '...'],
   symbol('ConditionalFunctions', 'Coalesce')],
]

# These functions are implemented against the UDF interface.
# TODO: this list should subsume the one above when all builtins are migrated.
udf_functions = [
  [['udf_pi'], 'DOUBLE', [],
   '_ZN6impala11UdfBuiltins2PiEPN10impala_udf15FunctionContextE'],
  [['udf_abs'], 'DOUBLE', ['DOUBLE'],
   '_ZN6impala11UdfBuiltins3AbsEPN10impala_udf15FunctionContextERKNS1_9DoubleValE'],
  [['udf_lower'], 'STRING', ['STRING'],
   '_ZN6impala11UdfBuiltins5LowerEPN10impala_udf15FunctionContextERKNS1_9StringValE'],
  [['max_int'], 'INT', [],
   '_ZN6impala11UdfBuiltins6MaxIntEPN10impala_udf15FunctionContextE'],
  [['max_tinyint'], 'TINYINT', [],
   '_ZN6impala11UdfBuiltins10MaxTinyIntEPN10impala_udf15FunctionContextE'],
  [['max_smallint'], 'SMALLINT', [],
   '_ZN6impala11UdfBuiltins11MaxSmallIntEPN10impala_udf15FunctionContextE'],
  [['max_bigint'], 'BIGINT', [],
   '_ZN6impala11UdfBuiltins9MaxBigIntEPN10impala_udf15FunctionContextE'],
  [['min_int'], 'INT', [],
   '_ZN6impala11UdfBuiltins6MinIntEPN10impala_udf15FunctionContextE'],
  [['min_tinyint'], 'TINYINT', [],
   '_ZN6impala11UdfBuiltins10MinTinyIntEPN10impala_udf15FunctionContextE'],
  [['min_smallint'], 'SMALLINT', [],
   '_ZN6impala11UdfBuiltins11MinSmallIntEPN10impala_udf15FunctionContextE'],
  [['min_bigint'], 'BIGINT', [],
   '_ZN6impala11UdfBuiltins9MinBigIntEPN10impala_udf15FunctionContextE'],
  [['is_nan'], 'BOOLEAN', ['DOUBLE'],
   '_ZN6impala11UdfBuiltins5IsNanEPN10impala_udf15FunctionContextERKNS1_9DoubleValE'],
  [['is_inf'], 'BOOLEAN', ['DOUBLE'],
   '_ZN6impala11UdfBuiltins5IsInfEPN10impala_udf15FunctionContextERKNS1_9DoubleValE'],
  [['trunc'], 'TIMESTAMP', ['TIMESTAMP', 'STRING'],
   '_ZN6impala11UdfBuiltins5TruncEPN10impala_udf15FunctionContextERKNS1_12TimestampValERKNS1_9StringValE',
   '_ZN6impala11UdfBuiltins12TruncPrepareEPN10impala_udf15FunctionContextENS2_18FunctionStateScopeE',
   '_ZN6impala11UdfBuiltins10TruncCloseEPN10impala_udf15FunctionContextENS2_18FunctionStateScopeE'],
  [['extract'], 'INT', ['TIMESTAMP', 'STRING'],
   '_ZN6impala11UdfBuiltins7ExtractEPN10impala_udf15FunctionContextERKNS1_12TimestampValERKNS1_9StringValE',
   '_ZN6impala11UdfBuiltins14ExtractPrepareEPN10impala_udf15FunctionContextENS2_18FunctionStateScopeE',
   '_ZN6impala11UdfBuiltins12ExtractCloseEPN10impala_udf15FunctionContextENS2_18FunctionStateScopeE'],

  [['madlib_encode_vector'], 'STRING', ['STRING'],
    '_ZN6impala11UdfBuiltins12EncodeVectorEPN10impala_udf15FunctionContextERKNS1_9StringValE'],
  [['madlib_decode_vector'], 'STRING', ['STRING'],
    '_ZN6impala11UdfBuiltins12DecodeVectorEPN10impala_udf15FunctionContextERKNS1_9StringValE'],
  [['madlib_print_vector'], 'STRING', ['STRING'],
    '_ZN6impala11UdfBuiltins11PrintVectorEPN10impala_udf15FunctionContextERKNS1_9StringValE'],
  [['madlib_vector'], 'STRING', ['DOUBLE', '...'],
    '_ZN6impala11UdfBuiltins8ToVectorEPN10impala_udf15FunctionContextEiPKNS1_9DoubleValE'],
  [['madlib_vector_get'], 'DOUBLE', ['BIGINT', 'STRING'],
    '_ZN6impala11UdfBuiltins9VectorGetEPN10impala_udf15FunctionContextERKNS1_9BigIntValERKNS1_9StringValE'],
  [['unix_timestamp'], 'INT', ['STRING'], '_ZN6impala18TimestampFunctions14UnixFromStringEPN10impala_udf15FunctionContextERKNS1_9StringValE'],
  [['year'], 'INT', ['TIMESTAMP'], '_ZN6impala18TimestampFunctions4YearEPN10impala_udf15FunctionContextERKNS1_12TimestampValE'],
  [['month'], 'INT', ['TIMESTAMP'], '_ZN6impala18TimestampFunctions5MonthEPN10impala_udf15FunctionContextERKNS1_12TimestampValE'],
[['dayofweek'], 'INT', ['TIMESTAMP'], '_ZN6impala18TimestampFunctions9DayOfWeekEPN10impala_udf15FunctionContextERKNS1_12TimestampValE'],
  [['day', 'dayofmonth'], 'INT', ['TIMESTAMP'], '_ZN6impala18TimestampFunctions10DayOfMonthEPN10impala_udf15FunctionContextERKNS1_12TimestampValE'],
  [['dayofyear'], 'INT', ['TIMESTAMP'], '_ZN6impala18TimestampFunctions9DayOfYearEPN10impala_udf15FunctionContextERKNS1_12TimestampValE'],
  [['weekofyear'], 'INT', ['TIMESTAMP'], '_ZN6impala18TimestampFunctions10WeekOfYearEPN10impala_udf15FunctionContextERKNS1_12TimestampValE'],
  [['hour'], 'INT', ['TIMESTAMP'], '_ZN6impala18TimestampFunctions4HourEPN10impala_udf15FunctionContextERKNS1_12TimestampValE'],
  [['minute'], 'INT', ['TIMESTAMP'], '_ZN6impala18TimestampFunctions6MinuteEPN10impala_udf15FunctionContextERKNS1_12TimestampValE'],
  [['second'], 'INT', ['TIMESTAMP'], '_ZN6impala18TimestampFunctions6SecondEPN10impala_udf15FunctionContextERKNS1_12TimestampValE'],
  [['to_date'], 'STRING', ['TIMESTAMP'], '_ZN6impala18TimestampFunctions6ToDateEPN10impala_udf15FunctionContextERKNS1_12TimestampValE'],
  [['dayname'], 'STRING', ['TIMESTAMP'], '_ZN6impala18TimestampFunctions7DayNameEPN10impala_udf15FunctionContextERKNS1_12TimestampValE'],
  [['years_add'], 'TIMESTAMP', ['TIMESTAMP', 'INT'],
      '_ZN6impala18TimestampFunctions10DateAddSubILb1EN10impala_udf6IntValEN5boost9date_time14years_durationINS4_9gregorian21greg_durations_configEEEEENS2_12TimestampValEPNS2_15FunctionContextERKSA_RKT0_'],
  [['years_add'], 'TIMESTAMP', ['TIMESTAMP', 'BIGINT'],
      '_ZN6impala18TimestampFunctions10DateAddSubILb1EN10impala_udf9BigIntValEN5boost9date_time14years_durationINS4_9gregorian21greg_durations_configEEEEENS2_12TimestampValEPNS2_15FunctionContextERKSA_RKT0_'],
  [['years_sub'], 'TIMESTAMP', ['TIMESTAMP', 'INT'],
      '_ZN6impala18TimestampFunctions10DateAddSubILb0EN10impala_udf6IntValEN5boost9date_time14years_durationINS4_9gregorian21greg_durations_configEEEEENS2_12TimestampValEPNS2_15FunctionContextERKSA_RKT0_'],
  [['years_sub'], 'TIMESTAMP', ['TIMESTAMP', 'BIGINT'],
      '_ZN6impala18TimestampFunctions10DateAddSubILb0EN10impala_udf9BigIntValEN5boost9date_time14years_durationINS4_9gregorian21greg_durations_configEEEEENS2_12TimestampValEPNS2_15FunctionContextERKSA_RKT0_'],
  [['months_add', 'add_months'], 'TIMESTAMP', ['TIMESTAMP', 'INT'],
      '_ZN6impala18TimestampFunctions10DateAddSubILb1EN10impala_udf6IntValEN5boost9date_time15months_durationINS4_9gregorian21greg_durations_configEEEEENS2_12TimestampValEPNS2_15FunctionContextERKSA_RKT0_'],
  [['months_add', 'add_months'], 'TIMESTAMP', ['TIMESTAMP', 'BIGINT'],
      '_ZN6impala18TimestampFunctions10DateAddSubILb1EN10impala_udf9BigIntValEN5boost9date_time15months_durationINS4_9gregorian21greg_durations_configEEEEENS2_12TimestampValEPNS2_15FunctionContextERKSA_RKT0_'],
  [['months_sub'], 'TIMESTAMP', ['TIMESTAMP', 'INT'],
      '_ZN6impala18TimestampFunctions10DateAddSubILb0EN10impala_udf6IntValEN5boost9date_time15months_durationINS4_9gregorian21greg_durations_configEEEEENS2_12TimestampValEPNS2_15FunctionContextERKSA_RKT0_'],
  [['months_sub'], 'TIMESTAMP', ['TIMESTAMP', 'BIGINT'],
      '_ZN6impala18TimestampFunctions10DateAddSubILb0EN10impala_udf9BigIntValEN5boost9date_time15months_durationINS4_9gregorian21greg_durations_configEEEEENS2_12TimestampValEPNS2_15FunctionContextERKSA_RKT0_'],
  [['weeks_add'], 'TIMESTAMP', ['TIMESTAMP', 'INT'],
      '_ZN6impala18TimestampFunctions10DateAddSubILb1EN10impala_udf6IntValEN5boost9gregorian14weeks_durationEEENS2_12TimestampValEPNS2_15FunctionContextERKS7_RKT0_'],
  [['weeks_add'], 'TIMESTAMP', ['TIMESTAMP', 'BIGINT'],
      '_ZN6impala18TimestampFunctions10DateAddSubILb1EN10impala_udf9BigIntValEN5boost9gregorian14weeks_durationEEENS2_12TimestampValEPNS2_15FunctionContextERKS7_RKT0_'],
  [['weeks_sub'], 'TIMESTAMP', ['TIMESTAMP', 'INT'],
      '_ZN6impala18TimestampFunctions10DateAddSubILb0EN10impala_udf6IntValEN5boost9gregorian14weeks_durationEEENS2_12TimestampValEPNS2_15FunctionContextERKS7_RKT0_'],
  [['weeks_sub'], 'TIMESTAMP', ['TIMESTAMP', 'BIGINT'],
      '_ZN6impala18TimestampFunctions10DateAddSubILb0EN10impala_udf9BigIntValEN5boost9gregorian14weeks_durationEEENS2_12TimestampValEPNS2_15FunctionContextERKS7_RKT0_'],
  [['days_add', 'date_add', 'adddate'], 'TIMESTAMP', ['TIMESTAMP', 'INT'],
      '_ZN6impala18TimestampFunctions10DateAddSubILb1EN10impala_udf6IntValEN5boost9gregorian13date_durationEEENS2_12TimestampValEPNS2_15FunctionContextERKS7_RKT0_'],
  [['days_add', 'date_add', 'adddate'], 'TIMESTAMP', ['TIMESTAMP', 'BIGINT'],
      '_ZN6impala18TimestampFunctions10DateAddSubILb1EN10impala_udf9BigIntValEN5boost9gregorian13date_durationEEENS2_12TimestampValEPNS2_15FunctionContextERKS7_RKT0_'],
  [['days_sub', 'date_sub', 'subdate'], 'TIMESTAMP', ['TIMESTAMP', 'INT'],
      '_ZN6impala18TimestampFunctions10DateAddSubILb0EN10impala_udf6IntValEN5boost9gregorian13date_durationEEENS2_12TimestampValEPNS2_15FunctionContextERKS7_RKT0_'],
  [['days_sub', 'date_sub', 'subdate'], 'TIMESTAMP', ['TIMESTAMP', 'BIGINT'],
      '_ZN6impala18TimestampFunctions10DateAddSubILb0EN10impala_udf9BigIntValEN5boost9gregorian13date_durationEEENS2_12TimestampValEPNS2_15FunctionContextERKS7_RKT0_'],
  [['hours_add'], 'TIMESTAMP', ['TIMESTAMP', 'INT'],
      '_ZN6impala18TimestampFunctions10TimeAddSubILb1EN10impala_udf6IntValEN5boost10posix_time5hoursEEENS2_12TimestampValEPNS2_15FunctionContextERKS7_RKT0_'],
  [['hours_add'], 'TIMESTAMP', ['TIMESTAMP', 'BIGINT'],
      '_ZN6impala18TimestampFunctions10TimeAddSubILb1EN10impala_udf9BigIntValEN5boost10posix_time5hoursEEENS2_12TimestampValEPNS2_15FunctionContextERKS7_RKT0_'],
  [['hours_sub'], 'TIMESTAMP', ['TIMESTAMP', 'INT'],
      '_ZN6impala18TimestampFunctions10TimeAddSubILb0EN10impala_udf6IntValEN5boost10posix_time5hoursEEENS2_12TimestampValEPNS2_15FunctionContextERKS7_RKT0_'],
  [['hours_sub'], 'TIMESTAMP', ['TIMESTAMP', 'BIGINT'],
      '_ZN6impala18TimestampFunctions10TimeAddSubILb0EN10impala_udf9BigIntValEN5boost10posix_time5hoursEEENS2_12TimestampValEPNS2_15FunctionContextERKS7_RKT0_'],
  [['minutes_add'], 'TIMESTAMP', ['TIMESTAMP', 'INT'],
      '_ZN6impala18TimestampFunctions10TimeAddSubILb1EN10impala_udf6IntValEN5boost10posix_time7minutesEEENS2_12TimestampValEPNS2_15FunctionContextERKS7_RKT0_'],
  [['minutes_add'], 'TIMESTAMP', ['TIMESTAMP', 'BIGINT'],
      '_ZN6impala18TimestampFunctions10TimeAddSubILb1EN10impala_udf9BigIntValEN5boost10posix_time7minutesEEENS2_12TimestampValEPNS2_15FunctionContextERKS7_RKT0_'],
  [['minutes_sub'], 'TIMESTAMP', ['TIMESTAMP', 'INT'],
      '_ZN6impala18TimestampFunctions10TimeAddSubILb0EN10impala_udf6IntValEN5boost10posix_time7minutesEEENS2_12TimestampValEPNS2_15FunctionContextERKS7_RKT0_'],
  [['minutes_sub'], 'TIMESTAMP', ['TIMESTAMP', 'BIGINT'],
      '_ZN6impala18TimestampFunctions10TimeAddSubILb0EN10impala_udf9BigIntValEN5boost10posix_time7minutesEEENS2_12TimestampValEPNS2_15FunctionContextERKS7_RKT0_'],
  [['seconds_add'], 'TIMESTAMP', ['TIMESTAMP', 'INT'],
      '_ZN6impala18TimestampFunctions10TimeAddSubILb1EN10impala_udf6IntValEN5boost10posix_time7secondsEEENS2_12TimestampValEPNS2_15FunctionContextERKS7_RKT0_'],
  [['seconds_add'], 'TIMESTAMP', ['TIMESTAMP', 'BIGINT'],
      '_ZN6impala18TimestampFunctions10TimeAddSubILb1EN10impala_udf9BigIntValEN5boost10posix_time7secondsEEENS2_12TimestampValEPNS2_15FunctionContextERKS7_RKT0_'],
  [['seconds_sub'], 'TIMESTAMP', ['TIMESTAMP', 'INT'],
      '_ZN6impala18TimestampFunctions10TimeAddSubILb0EN10impala_udf6IntValEN5boost10posix_time7secondsEEENS2_12TimestampValEPNS2_15FunctionContextERKS7_RKT0_'],
  [['seconds_sub'], 'TIMESTAMP', ['TIMESTAMP', 'BIGINT'],
      '_ZN6impala18TimestampFunctions10TimeAddSubILb0EN10impala_udf9BigIntValEN5boost10posix_time7secondsEEENS2_12TimestampValEPNS2_15FunctionContextERKS7_RKT0_'],
  [['milliseconds_add'], 'TIMESTAMP', ['TIMESTAMP', 'INT'],
      '_ZN6impala18TimestampFunctions10TimeAddSubILb1EN10impala_udf6IntValEN5boost9date_time18subsecond_durationINS4_10posix_time13time_durationELl1000EEEEENS2_12TimestampValEPNS2_15FunctionContextERKSA_RKT0_'],
  [['milliseconds_add'], 'TIMESTAMP', ['TIMESTAMP', 'BIGINT'],
      '_ZN6impala18TimestampFunctions10TimeAddSubILb1EN10impala_udf9BigIntValEN5boost9date_time18subsecond_durationINS4_10posix_time13time_durationELl1000EEEEENS2_12TimestampValEPNS2_15FunctionContextERKSA_RKT0_'],
  [['milliseconds_sub'], 'TIMESTAMP', ['TIMESTAMP', 'INT'],
      '_ZN6impala18TimestampFunctions10TimeAddSubILb0EN10impala_udf6IntValEN5boost9date_time18subsecond_durationINS4_10posix_time13time_durationELl1000EEEEENS2_12TimestampValEPNS2_15FunctionContextERKSA_RKT0_'],
  [['milliseconds_sub'], 'TIMESTAMP', ['TIMESTAMP', 'BIGINT'],
      '_ZN6impala18TimestampFunctions10TimeAddSubILb0EN10impala_udf9BigIntValEN5boost9date_time18subsecond_durationINS4_10posix_time13time_durationELl1000EEEEENS2_12TimestampValEPNS2_15FunctionContextERKSA_RKT0_'],
  [['microseconds_add'], 'TIMESTAMP', ['TIMESTAMP', 'INT'],
      '_ZN6impala18TimestampFunctions10TimeAddSubILb1EN10impala_udf6IntValEN5boost9date_time18subsecond_durationINS4_10posix_time13time_durationELl1000000EEEEENS2_12TimestampValEPNS2_15FunctionContextERKSA_RKT0_'],
  [['microseconds_add'], 'TIMESTAMP', ['TIMESTAMP', 'BIGINT'],
      '_ZN6impala18TimestampFunctions10TimeAddSubILb1EN10impala_udf9BigIntValEN5boost9date_time18subsecond_durationINS4_10posix_time13time_durationELl1000000EEEEENS2_12TimestampValEPNS2_15FunctionContextERKSA_RKT0_'],
  [['microseconds_sub'], 'TIMESTAMP', ['TIMESTAMP', 'INT'],
      '_ZN6impala18TimestampFunctions10TimeAddSubILb0EN10impala_udf6IntValEN5boost9date_time18subsecond_durationINS4_10posix_time13time_durationELl1000000EEEEENS2_12TimestampValEPNS2_15FunctionContextERKSA_RKT0_'],
  [['microseconds_sub'], 'TIMESTAMP', ['TIMESTAMP', 'BIGINT'],
      '_ZN6impala18TimestampFunctions10TimeAddSubILb0EN10impala_udf9BigIntValEN5boost9date_time18subsecond_durationINS4_10posix_time13time_durationELl1000000EEEEENS2_12TimestampValEPNS2_15FunctionContextERKSA_RKT0_'],
  [['nanoseconds_add'], 'TIMESTAMP', ['TIMESTAMP', 'INT'],
      '_ZN6impala18TimestampFunctions10TimeAddSubILb1EN10impala_udf6IntValEN5boost9date_time18subsecond_durationINS4_10posix_time13time_durationELl1000000000EEEEENS2_12TimestampValEPNS2_15FunctionContextERKSA_RKT0_'],
  [['nanoseconds_add'], 'TIMESTAMP', ['TIMESTAMP', 'BIGINT'],
      '_ZN6impala18TimestampFunctions10TimeAddSubILb1EN10impala_udf9BigIntValEN5boost9date_time18subsecond_durationINS4_10posix_time13time_durationELl1000000000EEEEENS2_12TimestampValEPNS2_15FunctionContextERKSA_RKT0_'],
  [['nanoseconds_sub'], 'TIMESTAMP', ['TIMESTAMP', 'INT'],
      '_ZN6impala18TimestampFunctions10TimeAddSubILb0EN10impala_udf6IntValEN5boost9date_time18subsecond_durationINS4_10posix_time13time_durationELl1000000000EEEEENS2_12TimestampValEPNS2_15FunctionContextERKSA_RKT0_'],
  [['nanoseconds_sub'], 'TIMESTAMP', ['TIMESTAMP', 'BIGINT'],
      '_ZN6impala18TimestampFunctions10TimeAddSubILb0EN10impala_udf9BigIntValEN5boost9date_time18subsecond_durationINS4_10posix_time13time_durationELl1000000000EEEEENS2_12TimestampValEPNS2_15FunctionContextERKSA_RKT0_'],
  [['datediff'], 'INT', ['TIMESTAMP', 'TIMESTAMP'], '_ZN6impala18TimestampFunctions8DateDiffEPN10impala_udf15FunctionContextERKNS1_12TimestampValES6_'],
   [['unix_timestamp'], 'INT', [], '_ZN6impala18TimestampFunctions4UnixEPN10impala_udf15FunctionContextE'],
  [['unix_timestamp'], 'INT', ['TIMESTAMP'], '_ZN6impala18TimestampFunctions4UnixEPN10impala_udf15FunctionContextERKNS1_12TimestampValE'],
  [['unix_timestamp'], 'INT', ['STRING', 'STRING'], '_ZN6impala18TimestampFunctions4UnixEPN10impala_udf15FunctionContextERKNS1_9StringValES6_',
          '_ZN6impala18TimestampFunctions22UnixAndFromUnixPrepareEPN10impala_udf15FunctionContextENS2_18FunctionStateScopeE',
          '_ZN6impala18TimestampFunctions20UnixAndFromUnixCloseEPN10impala_udf15FunctionContextENS2_18FunctionStateScopeE'],
  [['from_unixtime'], 'STRING', ['INT'],
      '_ZN6impala18TimestampFunctions8FromUnixIN10impala_udf6IntValEEENS2_9StringValEPNS2_15FunctionContextERKT_'],
  [['from_unixtime'], 'STRING', ['INT', 'STRING'],
      '_ZN6impala18TimestampFunctions8FromUnixIN10impala_udf6IntValEEENS2_9StringValEPNS2_15FunctionContextERKT_RKS4_',
      '_ZN6impala18TimestampFunctions22UnixAndFromUnixPrepareEPN10impala_udf15FunctionContextENS2_18FunctionStateScopeE',
     '_ZN6impala18TimestampFunctions20UnixAndFromUnixCloseEPN10impala_udf15FunctionContextENS2_18FunctionStateScopeE'],
  [['from_unixtime'], 'STRING', ['BIGINT'],
      '_ZN6impala18TimestampFunctions8FromUnixIN10impala_udf9BigIntValEEENS2_9StringValEPNS2_15FunctionContextERKT_'],
  [['from_unixtime'], 'STRING', ['BIGINT', 'STRING'],
      '_ZN6impala18TimestampFunctions8FromUnixIN10impala_udf9BigIntValEEENS2_9StringValEPNS2_15FunctionContextERKT_RKS4_',
      '_ZN6impala18TimestampFunctions22UnixAndFromUnixPrepareEPN10impala_udf15FunctionContextENS2_18FunctionStateScopeE',
      '_ZN6impala18TimestampFunctions20UnixAndFromUnixCloseEPN10impala_udf15FunctionContextENS2_18FunctionStateScopeE'],
  [['now', 'current_timestamp'], 'TIMESTAMP', [], '_ZN6impala18TimestampFunctions3NowEPN10impala_udf15FunctionContextE'],

  # Math builtin functions
  [['pi'], 'DOUBLE', [], 'impala::MathFunctions::Pi'],
  [['e'], 'DOUBLE', [], 'impala::MathFunctions::E'],
  [['abs'], 'DOUBLE', ['DOUBLE'], 'impala::MathFunctions::Abs'],
  [['sign'], 'FLOAT', ['DOUBLE'], 'impala::MathFunctions::Sign'],
  [['sin'], 'DOUBLE', ['DOUBLE'], 'impala::MathFunctions::Sin'],
  [['asin'], 'DOUBLE', ['DOUBLE'], 'impala::MathFunctions::Asin'],
  [['cos'], 'DOUBLE', ['DOUBLE'], 'impala::MathFunctions::Cos'],
  [['acos'], 'DOUBLE', ['DOUBLE'], 'impala::MathFunctions::Acos'],
  [['tan'], 'DOUBLE', ['DOUBLE'], 'impala::MathFunctions::Tan'],
  [['atan'], 'DOUBLE', ['DOUBLE'], 'impala::MathFunctions::Atan'],
  [['radians'], 'DOUBLE', ['DOUBLE'], 'impala::MathFunctions::Radians'],
  [['degrees'], 'DOUBLE', ['DOUBLE'], 'impala::MathFunctions::Degrees'],
  [['ceil', 'ceiling'], 'BIGINT', ['DOUBLE'], 'impala::MathFunctions::Ceil'],
  [['floor'], 'BIGINT', ['DOUBLE'], 'impala::MathFunctions::Floor'],
  [['round'], 'BIGINT', ['DOUBLE'], 'impala::MathFunctions::Round'],
  [['round'], 'DOUBLE', ['DOUBLE', 'INT'], 'impala::MathFunctions::RoundUpTo'],
  [['exp'], 'DOUBLE', ['DOUBLE'], 'impala::MathFunctions::Exp'],
  [['ln'], 'DOUBLE', ['DOUBLE'], 'impala::MathFunctions::Ln'],
  [['log10'], 'DOUBLE', ['DOUBLE'], 'impala::MathFunctions::Log10'],
  [['log2'], 'DOUBLE', ['DOUBLE'], 'impala::MathFunctions::Log2'],
  [['log'], 'DOUBLE', ['DOUBLE', 'DOUBLE'], 'impala::MathFunctions::Log'],
  [['pow', 'power'], 'DOUBLE', ['DOUBLE', 'DOUBLE'], 'impala::MathFunctions::Pow'],
  [['sqrt'], 'DOUBLE', ['DOUBLE'], 'impala::MathFunctions::Sqrt'],
  [['rand'], 'DOUBLE', [], 'impala::MathFunctions::Rand',
   '_ZN6impala13MathFunctions11RandPrepareEPN10impala_udf15FunctionContextENS2_18FunctionStateScopeE'],
  [['rand'], 'DOUBLE', ['BIGINT'], 'impala::MathFunctions::RandSeed',
   '_ZN6impala13MathFunctions11RandPrepareEPN10impala_udf15FunctionContextENS2_18FunctionStateScopeE'],
  [['bin'], 'STRING', ['BIGINT'], 'impala::MathFunctions::Bin'],
  [['hex'], 'STRING', ['BIGINT'], 'impala::MathFunctions::HexInt'],
  [['hex'], 'STRING', ['STRING'], 'impala::MathFunctions::HexString'],
  [['unhex'], 'STRING', ['STRING'], 'impala::MathFunctions::Unhex'],
  [['conv'], 'STRING', ['BIGINT', 'TINYINT', 'TINYINT'],
   'impala::MathFunctions::ConvInt'],
  [['conv'], 'STRING', ['STRING', 'TINYINT', 'TINYINT'],
      'impala::MathFunctions::ConvString'],
  [['pmod'], 'BIGINT', ['BIGINT', 'BIGINT'], 'impala::MathFunctions::PmodBigInt'],
  [['pmod'], 'DOUBLE', ['DOUBLE', 'DOUBLE'], 'impala::MathFunctions::PmodDouble'],
  [['fmod'], 'FLOAT', ['FLOAT', 'FLOAT'], 'impala::MathFunctions::FmodFloat'],
  [['fmod'], 'DOUBLE', ['DOUBLE', 'DOUBLE'], 'impala::MathFunctions::FmodDouble'],
  [['positive'], 'TINYINT', ['TINYINT'],
   '_ZN6impala13MathFunctions8PositiveIN10impala_udf10TinyIntValEEET_PNS2_15FunctionContextERKS4_'],
  [['positive'], 'SMALLINT', ['SMALLINT'],
   '_ZN6impala13MathFunctions8PositiveIN10impala_udf11SmallIntValEEET_PNS2_15FunctionContextERKS4_'],
  [['positive'], 'INT', ['INT'],
   '_ZN6impala13MathFunctions8PositiveIN10impala_udf6IntValEEET_PNS2_15FunctionContextERKS4_'],
  [['positive'], 'BIGINT', ['BIGINT'],
   '_ZN6impala13MathFunctions8PositiveIN10impala_udf9BigIntValEEET_PNS2_15FunctionContextERKS4_'],
  [['positive'], 'FLOAT', ['FLOAT'],
   '_ZN6impala13MathFunctions8PositiveIN10impala_udf8FloatValEEET_PNS2_15FunctionContextERKS4_'],
  [['positive'], 'DOUBLE', ['DOUBLE'],
   '_ZN6impala13MathFunctions8PositiveIN10impala_udf9DoubleValEEET_PNS2_15FunctionContextERKS4_'],
  [['positive'], 'DECIMAL', ['DECIMAL'],
   '_ZN6impala13MathFunctions8PositiveIN10impala_udf10DecimalValEEET_PNS2_15FunctionContextERKS4_'],
  [['negative'], 'TINYINT', ['TINYINT'],
   '_ZN6impala13MathFunctions8NegativeIN10impala_udf10TinyIntValEEET_PNS2_15FunctionContextERKS4_'],
  [['negative'], 'SMALLINT', ['SMALLINT'],
   '_ZN6impala13MathFunctions8NegativeIN10impala_udf11SmallIntValEEET_PNS2_15FunctionContextERKS4_'],
  [['negative'], 'INT', ['INT'],
   '_ZN6impala13MathFunctions8NegativeIN10impala_udf6IntValEEET_PNS2_15FunctionContextERKS4_'],
  [['negative'], 'BIGINT', ['BIGINT'],
   '_ZN6impala13MathFunctions8NegativeIN10impala_udf9BigIntValEEET_PNS2_15FunctionContextERKS4_'],
  [['negative'], 'FLOAT', ['FLOAT'],
   '_ZN6impala13MathFunctions8NegativeIN10impala_udf8FloatValEEET_PNS2_15FunctionContextERKS4_'],
  [['negative'], 'DOUBLE', ['DOUBLE'],
   '_ZN6impala13MathFunctions8NegativeIN10impala_udf9DoubleValEEET_PNS2_15FunctionContextERKS4_'],
  [['negative'], 'DECIMAL', ['DECIMAL'],
   '_ZN6impala13MathFunctions8NegativeIN10impala_udf10DecimalValEEET_PNS2_15FunctionContextERKS4_'],
  [['quotient'], 'BIGINT', ['BIGINT', 'BIGINT'],
      'impala::MathFunctions::QuotientBigInt'],
  [['quotient'], 'BIGINT', ['DOUBLE', 'DOUBLE'],
      'impala::MathFunctions::QuotientDouble'],
  [['least'], 'TINYINT', ['TINYINT', '...'],
   '_ZN6impala13MathFunctions13LeastGreatestIN10impala_udf10TinyIntValELb1EEET_PNS2_15FunctionContextEiPKS4_'],
  [['least'], 'SMALLINT', ['SMALLINT', '...'],
   '_ZN6impala13MathFunctions13LeastGreatestIN10impala_udf11SmallIntValELb1EEET_PNS2_15FunctionContextEiPKS4_'],
  [['least'], 'INT', ['INT', '...'],
   '_ZN6impala13MathFunctions13LeastGreatestIN10impala_udf6IntValELb1EEET_PNS2_15FunctionContextEiPKS4_'],
  [['least'], 'BIGINT', ['BIGINT', '...'],
   '_ZN6impala13MathFunctions13LeastGreatestIN10impala_udf9BigIntValELb1EEET_PNS2_15FunctionContextEiPKS4_'],
  [['least'], 'FLOAT', ['FLOAT', '...'],
   '_ZN6impala13MathFunctions13LeastGreatestIN10impala_udf8FloatValELb1EEET_PNS2_15FunctionContextEiPKS4_'],
  [['least'], 'DOUBLE', ['DOUBLE', '...'],
   '_ZN6impala13MathFunctions13LeastGreatestIN10impala_udf9DoubleValELb1EEET_PNS2_15FunctionContextEiPKS4_'],
  [['least'], 'TIMESTAMP', ['TIMESTAMP', '...'],
   '_ZN6impala13MathFunctions13LeastGreatestILb1EEEN10impala_udf12TimestampValEPNS2_15FunctionContextEiPKS3_'],
  [['least'], 'STRING', ['STRING', '...'],
   '_ZN6impala13MathFunctions13LeastGreatestILb1EEEN10impala_udf9StringValEPNS2_15FunctionContextEiPKS3_'],
  [['least'], 'DECIMAL', ['DECIMAL', '...'],
   '_ZN6impala13MathFunctions13LeastGreatestILb1EEEN10impala_udf10DecimalValEPNS2_15FunctionContextEiPKS3_'],
  [['greatest'], 'TINYINT', ['TINYINT', '...'],
   '_ZN6impala13MathFunctions13LeastGreatestIN10impala_udf10TinyIntValELb0EEET_PNS2_15FunctionContextEiPKS4_'],
  [['greatest'], 'SMALLINT', ['SMALLINT', '...'],
   '_ZN6impala13MathFunctions13LeastGreatestIN10impala_udf11SmallIntValELb0EEET_PNS2_15FunctionContextEiPKS4_'],
  [['greatest'], 'INT', ['INT', '...'],
   '_ZN6impala13MathFunctions13LeastGreatestIN10impala_udf6IntValELb0EEET_PNS2_15FunctionContextEiPKS4_'],
  [['greatest'], 'BIGINT', ['BIGINT', '...'],
   '_ZN6impala13MathFunctions13LeastGreatestIN10impala_udf9BigIntValELb0EEET_PNS2_15FunctionContextEiPKS4_'],
  [['greatest'], 'FLOAT', ['FLOAT', '...'],
   '_ZN6impala13MathFunctions13LeastGreatestIN10impala_udf8FloatValELb0EEET_PNS2_15FunctionContextEiPKS4_'],
  [['greatest'], 'DOUBLE', ['DOUBLE', '...'],
   '_ZN6impala13MathFunctions13LeastGreatestIN10impala_udf9DoubleValELb0EEET_PNS2_15FunctionContextEiPKS4_'],
  [['greatest'], 'TIMESTAMP', ['TIMESTAMP', '...'],
   '_ZN6impala13MathFunctions13LeastGreatestILb0EEEN10impala_udf12TimestampValEPNS2_15FunctionContextEiPKS3_'],
  [['greatest'], 'STRING', ['STRING', '...'],
   '_ZN6impala13MathFunctions13LeastGreatestILb0EEEN10impala_udf9StringValEPNS2_15FunctionContextEiPKS3_'],
  [['greatest'], 'DECIMAL', ['DECIMAL', '...'],
   '_ZN6impala13MathFunctions13LeastGreatestILb0EEEN10impala_udf10DecimalValEPNS2_15FunctionContextEiPKS3_'],

  # Decimal Functions
  # TODO: oracle has decimal support for transcendental functions (e.g. sin()) to very
  # high precisions. Do we need them? It's unclear if other databases do the same.
  [['precision'], 'INT', ['DECIMAL'], 'impala::DecimalFunctions::Precision'],
  [['scale'], 'INT', ['DECIMAL'], 'impala::DecimalFunctions::Scale'],
  [['abs'], 'DECIMAL', ['DECIMAL'], 'impala::DecimalFunctions::Abs'],
  [['ceil', 'ceiling'], 'DECIMAL', ['DECIMAL'], 'impala::DecimalFunctions::Ceil'],
  [['floor'], 'DECIMAL', ['DECIMAL'], 'impala::DecimalFunctions::Floor'],
  [['round'], 'DECIMAL', ['DECIMAL'], 'impala::DecimalFunctions::Round'],
  [['round'], 'DECIMAL', ['DECIMAL', 'TINYINT'], 'impala::DecimalFunctions::RoundTo'],
  [['round'], 'DECIMAL', ['DECIMAL', 'SMALLINT'], 'impala::DecimalFunctions::RoundTo'],
  [['round'], 'DECIMAL', ['DECIMAL', 'INT'], 'impala::DecimalFunctions::RoundTo'],
  [['round'], 'DECIMAL', ['DECIMAL', 'BIGINT'], 'impala::DecimalFunctions::RoundTo'],
  [['truncate'], 'DECIMAL', ['DECIMAL'], 'impala::DecimalFunctions::Truncate'],
  [['truncate'], 'DECIMAL', ['DECIMAL', 'TINYINT'],
      'impala::DecimalFunctions::TruncateTo'],
  [['truncate'], 'DECIMAL', ['DECIMAL', 'SMALLINT'],
      'impala::DecimalFunctions::TruncateTo'],
  [['truncate'], 'DECIMAL', ['DECIMAL', 'INT'],
      'impala::DecimalFunctions::TruncateTo'],
  [['truncate'], 'DECIMAL', ['DECIMAL', 'BIGINT'],
      'impala::DecimalFunctions::TruncateTo'],
]
