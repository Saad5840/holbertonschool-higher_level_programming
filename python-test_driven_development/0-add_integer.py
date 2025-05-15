#!/usr/bin/python3
"""
This module provides a function to add two integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats (after casting to int).

    Args:
        a: first number (int or float)
        b: second number (int or float, default is 98)

    Returns:
        The sum of a and b as an integer.

    Raises:
        TypeError: If a or b are not integers or floats

    Doctest examples:
    >>> add_integer(1, 2)
    3
    >>> add_integer(100, -2)
    98
    >>> add_integer(2)
    100
    >>> add_integer(100.3, -2)
    98
    >>> add_integer(4, "School")
    Traceback (most recent call last):
    TypeError: b must be an integer
    >>> add_integer(None)
    Traceback (most recent call last):
    TypeError: a must be an integer
    >>> add_integer("School", 5)
    Traceback (most recent call last):
    TypeError: a must be an integer
    >>> add_integer(3.7, 4.3)
    7
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
