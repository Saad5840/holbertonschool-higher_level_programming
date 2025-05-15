#!/usr/bin/python3
"""
Module to find the max integer in a list.
"""


def max_integer(list=[]):
    """
    Function to find and return the max integer in a list of integers.

    Args:
        list (list): List of integers or floats.

    Returns:
        int or float or None: The max integer/float in the list or None if list is empty.
    """
    if len(list) == 0:
        return None
    result = list[0]
    for item in list[1:]:
        if item > result:
            result = item
    return result
