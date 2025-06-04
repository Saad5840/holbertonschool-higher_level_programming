#!/usr/bin/python3
"""
Basic Serialization Module

Provides functions to serialize a dictionary to a JSON file
and deserialize JSON data back into a dictionary.
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serializes a dictionary and saves it to a JSON file.

    Args:
        data (dict): The dictionary to serialize.
        filename (str): The name of the file to save the JSON data.
    """
    with open(filename, 'w') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Loads and deserializes JSON data from a file into a dictionary.

    Args:
        filename (str): The name of the JSON file to read from.

    Returns:
        dict: The deserialized dictionary.
    """
    with open(filename, 'r') as f:
        return json.load(f)
