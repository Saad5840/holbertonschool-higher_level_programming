#!/usr/bin/python3
"""
This module provides a function to add two integers.
The function handles type checking and conversion from float to int.
"""


def add_integer(a, b=98):
    """
    Adds two integers after type checking and conversion.

    Args:
        a: First number, must be integer or float
        b: Second number, must be integer or float (default 98)

    Returns:
        The sum of a and b as an integer

    Raises:
        TypeError: If either a or b is not an integer or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    return int(a) + int(b)
