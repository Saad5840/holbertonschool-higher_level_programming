#!/usr/bin/python3
"""
This module provides a function that adds two integers.

It handles type validation and supports float-to-int conversion.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats (casted to integers).
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
