#!/usr/bin/python3
"""
This module provides a function that checks if an object
is exactly an instance of a specified class.
"""


def is_same_class(obj, a_class):
    """
    Return True if obj is exactly an instance of a_class.
    Return False otherwise.
    """
    return type(obj) is a_class
