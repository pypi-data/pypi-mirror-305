"""
Casting Expert - A comprehensive Python package for type casting and conversion

This package provides robust tools for handling type conversions,
with built-in validation and error handling.
"""

from .validators import validate_input
from .core import safe_cast, cast_to_type
from .str_to_dict.parsers import parse_string_to_dict, ParsingError

__version__ = "0.1.5"
__all__ = ['safe_cast', 'cast_to_type', 'validate_input', 'parse_string_to_dict', 'ParsingError']