"""
Casting Expert - A comprehensive Python package for type casting and conversion

This package provides robust tools for handling type conversions,
with built-in validation and error handling.
"""

from .core import safe_cast, cast_to_type
from .validators import validate_input

__version__ = "0.1.0"
__all__ = ['safe_cast', 'cast_to_type', 'validate_input']