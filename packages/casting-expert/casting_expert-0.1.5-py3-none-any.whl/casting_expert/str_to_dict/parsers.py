import re
import json
from typing import Dict, Any

class ParsingError(Exception):
    """Custom exception for parsing errors."""
    print(Exception)
    pass

def fix_invalid_nesting(input_string: str) -> str:
    """Fix invalid nested dictionary syntax."""
    # Replace comma-separated object literals with proper key-value pairs
    pattern = r',\s*({[^}]+})'
    
    def replacer(match):
        nested_dict = match.group(1)
        # Extract content from nested dict
        content = nested_dict.strip('{}')
        # Create a new key-value pair
        return f', "nested": {nested_dict}'
    
    return re.sub(pattern, replacer, input_string)

def normalize_quotes(input_string: str) -> str:
    """Normalize quotes in the string to make it valid JSON."""
    # First, handle triple quotes
    if input_string.startswith("'''") and input_string.endswith("'''"):
        input_string = input_string[3:-3]
    elif input_string.startswith('"""') and input_string.endswith('"""'):
        input_string = input_string[3:-3]

    result = []
    in_string = False
    current_quote = None
    i = 0
    
    while i < len(input_string):
        char = input_string[i]
        
        if char in ['"', "'"] and (i == 0 or input_string[i-1] != '\\'):
            if not in_string:
                # Starting a string
                in_string = True
                current_quote = char
                result.append('"')  # Always use double quotes to start
            elif char == current_quote:
                # Ending current string
                in_string = False
                current_quote = None
                result.append('"')  # Always use double quotes to end
            else:
                # Different quote inside string, keep it
                result.append(char)
        else:
            result.append(char)
        i += 1
    
    return ''.join(result)

def parse_string_to_dict(input_string: str) -> Dict[str, Any]:
    """
    Convert a string representation of a dictionary to a Python dictionary.
    Handles mixed quotes and nested structures.
    
    Args:
        input_string: String to convert
        
    Returns:
        Dict containing the parsed data
        
    Raises:
        ParsingError: If parsing fails
    
    Examples:
        >>> parse_string_to_dict('{"name": "John", "age": 30}')
        {'name': 'John', 'age': 30}
        >>> parse_string_to_dict("{'name': 'John', 'age': 30, {'info': 'engineer'}}")
        {'name': 'John', 'age': 30, 'nested': {'info': 'engineer'}}
    """
    if not isinstance(input_string, str):
        raise ParsingError("Input must be a string")

    # Clean whitespace
    input_string = input_string.strip()
    if not input_string:
        return {}

    # Fix invalid nesting
    input_string = fix_invalid_nesting(input_string)
    
    # Normalize quotes
    try:
        normalized = normalize_quotes(input_string)
        return json.loads(normalized)
    except json.JSONDecodeError as e:
        raise ParsingError(f"Invalid dictionary format: {str(e)}")