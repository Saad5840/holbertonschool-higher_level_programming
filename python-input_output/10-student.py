#!/usr/bin/python3
"""Module that defines a Student class with optional JSON serialization."""


class Student:
    """Defines a student with first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve dictionary representation of the instance.

        If attrs is a list of strings, only those attributes are included.
        Otherwise, all attributes are returned.

        Args:
            attrs (list, optional): List of attribute names to retrieve.

        Returns:
            dict: Dictionary representation of the student instance.
        """
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            filtered = {}
            for attr in attrs:
                if hasattr(self, attr):
                    filtered[attr] = getattr(self, attr)
            return filtered
        return self.__dict__.copy()
