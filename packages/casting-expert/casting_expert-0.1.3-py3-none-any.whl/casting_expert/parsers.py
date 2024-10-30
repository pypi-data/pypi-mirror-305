import json
import ast
import re
from typing import Dict, Any, Union, Optional

class ParsingError(Exception):
    """Custom exception for parsing errors."""
    pass

def clean_string(s: str) -> str:
    """
    Clean and normalize string representation of dictionary.
    
    Args:
        s: Input string
        
    Returns:
        Cleaned string ready for parsing
    """
    # Remove whitespace and newlines
    s = s.strip()
    
    # If it's completely wrapped in extra quotes, remove them
    if (s.startswith("'''") and s.endswith("'''")) or \
       (s.startswith('"""') and s.endswith('"""')):
        s = s[3:-3]
    
    # Replace all single quotes with double quotes, but only if they're
    # not inside double quotes
    cleaned = ""
    in_double_quotes = False
    i = 0
    while i < len(s):
        if s[i] == '"' and (i == 0 or s[i-1] != '\\'):
            in_double_quotes = not in_double_quotes
            cleaned += s[i]
        elif s[i] == "'" and not in_double_quotes:
            cleaned += '"'
        else:
            cleaned += s[i]
        i += 1
    
    return cleaned

def normalize_dict_string(s: str) -> str:
    """
    Normalize dictionary string by ensuring consistent quote usage.
    
    Args:
        s: Input string
        
    Returns:
        Normalized string with consistent quotes
    """
    # First pass: identify and fix nested dictionaries
    def fix_nested(match):
        inner = match.group(1)
        # Recursively normalize inner dictionary
        return '{' + normalize_dict_string(inner) + '}'
    
    # Handle nested dictionaries
    pattern = r'{([^{}]+)}'
    while re.search(pattern, s):
        s = re.sub(pattern, fix_nested, s)
    
    # Replace boolean and null values
    s = re.sub(r'\btrue\b', 'true', s, flags=re.IGNORECASE)
    s = re.sub(r'\bfalse\b', 'false', s, flags=re.IGNORECASE)
    s = re.sub(r'\bnull\b', 'null', s, flags=re.IGNORECASE)
    
    return s

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

    # Clean and normalize the input string
    input_string = clean_string(input_string)
    input_string = normalize_dict_string(input_string)
    
    if not input_string:
        return {}

    # Try specialized parsing first
    try:
        # For nested structures, try ast.literal_eval first
        return ast.literal_eval(input_string)
    except (SyntaxError, ValueError):
        # If that fails, continue with other parsers
        pass

    if format == 'auto':
        parsers = [
            ('json', _parse_json),
            ('python', _parse_python_literal),
            ('query', _parse_query_string),
            ('key_value', _parse_key_value_pairs)
        ]
        
        errors = []
        for format_name, parser in parsers:
            try:
                result = parser(input_string)
                # Verify the result is a valid dictionary
                if isinstance(result, dict):
                    return result
            except Exception as e:
                errors.append(f"{format_name}: {str(e)}")
                continue
        
        raise ParsingError(f"Failed to parse string. Errors:\n" + "\n".join(errors))
    
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
        # Try to parse as JSON first
        return json.loads(input_string)
    except json.JSONDecodeError:
        # If that fails, try to normalize the string first
        try:
            normalized = input_string.replace("'", '"')
            return json.loads(normalized)
        except json.JSONDecodeError as e:
            raise ParsingError(f"Invalid JSON: {str(e)}")

def _parse_python_literal(input_string: str) -> Dict[str, Any]:
    """Parse Python literal string to dictionary."""
    try:
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