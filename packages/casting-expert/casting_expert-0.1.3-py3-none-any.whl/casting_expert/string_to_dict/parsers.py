"""
Parsers for converting various string formats to dictionaries.
"""

import json
import re
from typing import Dict, Any, Optional
from urllib.parse import parse_qs, urlparse

class ParsingError(Exception):
    """Custom exception for parsing errors."""
    pass

def parse_string_to_dict(input_string: str, format: str = 'auto') -> Dict[str, Any]:
    """
    Convert a string to a dictionary using the specified format or auto-detect.
    
    Args:
        input_string: String to convert
        format: One of 'auto', 'json', 'query', 'key_value', 'yaml_like'
    
    Returns:
        Dict containing the parsed data
    
    Raises:
        ParsingError: If parsing fails
    """
    if not input_string:
        return {}

    if format == 'auto':
        # Try different formats in order of likelihood
        parsers = [
            ('json', parse_json),
            ('query', parse_query_string),
            ('key_value', parse_key_value_pairs),
            ('yaml_like', parse_yaml_like)
        ]
        
        errors = []
        for format_name, parser in parsers:
            try:
                return parser(input_string)
            except Exception as e:
                errors.append(f"{format_name}: {str(e)}")
        
        raise ParsingError(f"Failed to parse string with any format. Errors: {', '.join(errors)}")
    
    # Use specified format
    format_parsers = {
        'json': parse_json,
        'query': parse_query_string,
        'key_value': parse_key_value_pairs,
        'yaml_like': parse_yaml_like
    }
    
    if format not in format_parsers:
        raise ValueError(f"Unsupported format: {format}")
    
    return format_parsers[format](input_string)

def parse_json(input_string: str) -> Dict[str, Any]:
    """
    Parse JSON string to dictionary.
    
    Args:
        input_string: JSON string
    
    Returns:
        Parsed dictionary
    
    Examples:
        >>> parse_json('{"name": "John", "age": 30}')
        {'name': 'John', 'age': 30}
    """
    try:
        return json.loads(input_string)
    except json.JSONDecodeError as e:
        raise ParsingError(f"Invalid JSON: {str(e)}")

def parse_query_string(input_string: str) -> Dict[str, Any]:
    """
    Parse URL query string to dictionary.
    
    Args:
        input_string: Query string (with or without leading '?')
    
    Returns:
        Parsed dictionary
    
    Examples:
        >>> parse_query_string('name=John&age=30')
        {'name': ['John'], 'age': ['30']}
        >>> parse_query_string('?name=John&age=30')
        {'name': ['John'], 'age': ['30']}
    """
    # Remove leading '?' if present
    if input_string.startswith('?'):
        input_string = input_string[1:]
    
    try:
        # Parse query string
        parsed = parse_qs(input_string, keep_blank_values=True)
        
        # Simplify single-item lists
        return {
            k: v[0] if len(v) == 1 else v
            for k, v in parsed.items()
        }
    except Exception as e:
        raise ParsingError(f"Invalid query string: {str(e)}")

def parse_key_value_pairs(input_string: str) -> Dict[str, Any]:
    """
    Parse key-value pair string to dictionary.
    Supports multiple formats:
    - key=value
    - key: value
    - key -> value
    
    Args:
        input_string: String with key-value pairs
    
    Returns:
        Parsed dictionary
    
    Examples:
        >>> parse_key_value_pairs('name=John\\nage=30')
        {'name': 'John', 'age': '30'}
        >>> parse_key_value_pairs('name: John\\nage: 30')
        {'name': 'John', 'age': '30'}
    """
    result = {}
    
    # Split into lines and process each line
    lines = input_string.strip().split('\n')
    
    # Regular expression for key-value patterns
    patterns = [
        r'^([^=:->]+)=(.*)$',  # key=value
        r'^([^=:->]+):(.*)$',  # key: value
        r'^([^=:->]+)->(.*)$'  # key->value
    ]
    
    for line in lines:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
            
        # Try each pattern
        matched = False
        for pattern in patterns:
            match = re.match(pattern, line)
            if match:
                key, value = match.groups()
                result[key.strip()] = value.strip()
                matched = True
                break
        
        if not matched:
            raise ParsingError(f"Invalid key-value pair: {line}")
    
    return result

def parse_yaml_like(input_string: str) -> Dict[str, Any]:
    """
    Parse YAML-like string to dictionary.
    Supports simple YAML-like format with basic types.
    
    Args:
        input_string: YAML-like string
    
    Returns:
        Parsed dictionary
    
    Examples:
        >>> parse_yaml_like('name: John\\nage: 30\\ndetails:\\n  city: NY\\n  zip: 10001')
        {'name': 'John', 'age': '30', 'details': {'city': 'NY', 'zip': '10001'}}
    """
    result = {}
    current_indent = 0
    current_dict = result
    dict_stack = []
    
    lines = input_string.strip().split('\n')
    
    for line in lines:
        if not line.strip() or line.strip().startswith('#'):
            continue
            
        # Calculate indent level
        indent = len(line) - len(line.lstrip())
        line = line.strip()
        
        # Check for key-value pair
        if ':' in line:
            key, value = line.split(':', 1)
            key = key.strip()
            value = value.strip()
            
            # Handle indentation changes
            if indent > current_indent:
                dict_stack.append(current_dict)
                current_dict = result[prev_key]
            elif indent < current_indent:
                for _ in range((current_indent - indent) // 2):
                    current_dict = dict_stack.pop()
            
            # Store key-value pair
            if value:
                current_dict[key] = value
            else:
                current_dict[key] = {}
                prev_key = key
            
            current_indent = indent
        else:
            raise ParsingError(f"Invalid YAML-like line: {line}")
    
    return result