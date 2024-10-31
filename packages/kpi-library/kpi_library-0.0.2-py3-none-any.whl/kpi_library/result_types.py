# kpi_library/result_types.py
from enum import Enum


class ResultTypes(Enum):
    # constants
    __LIST_MAP_STRING = 'List<Map<String,String>>'
    __LIST_MAP_SERIALIZABLE = 'List<Map<String,Serializable>>'

    # enum classes
    INT = 'Integer'
    FLOAT = 'Float'
    STRING = 'String'
    DATE = 'DateTime'
    TIMEDELTA = 'Timedelta'
    BOOL = 'Boolean'

    DISTRIBUTION_INT = __LIST_MAP_STRING
    DISTRIBUTION_FLOAT = __LIST_MAP_STRING

    BOX_PLOT = 'Map<String,String>'
    HISTOGRAM = __LIST_MAP_STRING

    LIST_STR = 'List<String>'

    CAT_DISTRIBUTION_INT = __LIST_MAP_SERIALIZABLE
    CAT_DISTRIBUTION_FLOAT = __LIST_MAP_SERIALIZABLE

    INFER_FREQUENCY = 'Map<String,Integer>'
    PLOT = __LIST_MAP_STRING

    CAT_BOX_PLOT = __LIST_MAP_SERIALIZABLE

    CROSS_TABULATION = __LIST_MAP_STRING
