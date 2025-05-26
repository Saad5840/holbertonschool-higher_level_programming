#!/usr/bin/python3
"""
This module defines a function that checks if an object is an instance
of a class that inherited (directly or indirectly) from the specified class.
"""


def inherits_from(obj, a_class):
    """
    Return True if obj is an instance of a subclass of a_class
    (excluding if it is exactly an instance of a_class), otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
