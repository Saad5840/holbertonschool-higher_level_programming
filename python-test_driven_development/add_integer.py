#!/usr/bin/python3
"""Module that defines a function to add two integers.

The function add_integer(a, b=98) adds two integers or floats (cast to int)
and returns their sum as an integer.

Raises:
    TypeError: if a or b is not an integer or float.
"""

def add_integer(a, b=98):
    """Add two integers a and b (or floats cast to int).

    Args:
        a (int or float): first number to add.
        b (int or float, optional): second number to add, defaults to 98.

    Raises:
        TypeError: if a or b is not an integer or float.

    Returns:
        int: sum of a and b cast to integers.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
