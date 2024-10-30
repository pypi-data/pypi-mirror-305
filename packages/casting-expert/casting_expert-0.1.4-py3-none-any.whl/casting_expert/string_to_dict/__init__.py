"""
String to dictionary conversion functionality.
"""

from .parsers import (
    parse_string_to_dict,
    parse_json,
    parse_query_string,
    parse_key_value_pairs,
    parse_yaml_like
)
from .parsers import parse_string_to_dict
from .type_inference import TypeInference
from .serializers import DictSerializer
from .validators import DictValidator, ValidationError

__all__ = [
    'parse_string_to_dict',
    'parse_json',
    'parse_yaml_like',
    'parse_query_string',
    'parse_key_value_pairs',
    'TypeInference',
    'DictSerializer',
    'DictValidator',
    'ValidationError'
]