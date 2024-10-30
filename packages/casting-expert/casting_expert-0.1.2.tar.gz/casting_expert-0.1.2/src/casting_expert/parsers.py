import json
import ast
from typing import Dict, Any, Union
from collections import OrderedDict

class ParsingError(Exception):
    """Custom exception for parsing errors."""
    pass

def parse_string_to_dict(input_string: str, format: str = 'auto') -> Dict[str, Any]:
    """
    Convert a string representation of a dictionary to a Python dictionary.
    
    Args:
        input_string: String to convert
        format: One of 'auto', 'json', 'python', 'query', 'key_value'
    
    Returns:
        Dict containing the parsed data
    
    Raises:
        ParsingError: If parsing fails
    
    Examples:
        >>> parse_string_to_dict('{"name": "John", "age": 30}')
        {'name': 'John', 'age': 30}
        >>> parse_string_to_dict("{'name': 'John', 'age': 30}")
        {'name': 'John', 'age': 30}
    """
    if not isinstance(input_string, str):
        raise ParsingError("Input must be a string")

    input_string = input_string.strip()
    
    if not input_string:
        return {}

    if format == 'auto':
        # Try different formats
        parsers = [
            ('json', _parse_json),
            ('python', _parse_python_literal),
            ('query', _parse_query_string),
            ('key_value', _parse_key_value_pairs)
        ]
        
        errors = []
        for format_name, parser in parsers:
            try:
                return parser(input_string)
            except Exception as e:
                errors.append(f"{format_name}: {str(e)}")
                continue
        
        raise ParsingError(f"Failed to parse string. Tried multiple formats:\n" + "\n".join(errors))
    
    # Use specified format
    format_parsers = {
        'json': _parse_json,
        'python': _parse_python_literal,
        'query': _parse_query_string,
        'key_value': _parse_key_value_pairs
    }
    
    if format not in format_parsers:
        raise ValueError(f"Unsupported format: {format}")
    
    return format_parsers[format](input_string)

def _parse_json(input_string: str) -> Dict[str, Any]:
    """Parse JSON string to dictionary."""
    try:
        return json.loads(input_string)
    except json.JSONDecodeError as e:
        raise ParsingError(f"Invalid JSON: {str(e)}")

def _parse_python_literal(input_string: str) -> Dict[str, Any]:
    """Parse Python literal string to dictionary."""
    try:
        # Replace single quotes with double quotes for consistency
        if input_string.startswith("'") and input_string.endswith("'"):
            input_string = input_string[1:-1]
        
        # Use ast.literal_eval for safe parsing
        result = ast.literal_eval(input_string)
        
        if not isinstance(result, dict):
            raise ParsingError("Parsed result is not a dictionary")
        
        return result
    except (SyntaxError, ValueError) as e:
        raise ParsingError(f"Invalid Python literal: {str(e)}")

def _parse_query_string(input_string: str) -> Dict[str, Any]:
    """Parse URL query string to dictionary."""
    if not input_string or '=' not in input_string:
        raise ParsingError("Invalid query string format")
    
    result = {}
    pairs = input_string.split('&')
    
    for pair in pairs:
        if '=' not in pair:
            continue
        key, value = pair.split('=', 1)
        key = key.strip()
        value = value.strip()
        
        # Handle repeated keys as lists
        if key in result:
            if isinstance(result[key], list):
                result[key].append(value)
            else:
                result[key] = [result[key], value]
        else:
            result[key] = value
    
    return result

def _parse_key_value_pairs(input_string: str) -> Dict[str, Any]:
    """Parse key-value pair string to dictionary."""
    result = {}
    
    # Split by lines and handle different separators
    lines = input_string.split('\n')
    separators = [':', '=', '->']
    
    for line in lines:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
            
        # Try each separator
        for sep in separators:
            if sep in line:
                key, value = line.split(sep, 1)
                key = key.strip()
                value = value.strip()
                
                # Remove quotes if present
                if value.startswith(('"', "'")) and value.endswith(('"', "'")):
                    value = value[1:-1]
                
                result[key] = value
                break
        else:
            # No separator found
            result[line] = ''
    
    return result