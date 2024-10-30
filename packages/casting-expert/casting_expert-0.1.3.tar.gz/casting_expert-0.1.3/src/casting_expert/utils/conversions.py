"""
Utility functions for common type conversions.
"""

def str_to_bool(value: str) -> bool:
    """
    Convert a string to a boolean value.
    
    Args:
        value: String to convert
    
    Returns:
        bool: Converted boolean value
    """
    return value.lower() in ('true', '1', 'yes', 'y', 'on')