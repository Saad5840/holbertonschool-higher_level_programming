#!/usr/bin/python3


"""Module that defines a function to return JSON-serializable dictionary of an object."""


def class_to_json(obj):
    """Returns the dictionary description with simple data structure
    for JSON serialization of an object."""
    return obj.__dict__

