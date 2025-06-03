#!/usr/bin/python3
"""Defines a Student class with JSON serialization and deserialization."""


class Student:
    """Represents a student with basic attributes."""

    def __init__(self, first_name, last_name, age):
        """Initialize the Student instance.

        Args:
            first_name (str): First name of the student.
            last_name (str): Last name of the student.
            age (int): Age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve dictionary representation of the Student instance.

        Args:
            attrs (list, optional): List of attribute names to include.
                If None, all attributes are included.

        Returns:
            dict: Dictionary representation of the student instance.
        """
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            result = {}
            for attr in attrs:
                if hasattr(self, attr):
                    result[attr] = getattr(self, attr)
            return result
        return self.__dict__.copy()

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance with those in json.

        Args:
            json (dict): Dictionary with keys as attribute
                names and values as attribute values.
        """
        for key, value in json.items():
            setattr(self, key, value)
