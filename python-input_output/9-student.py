#!/usr/bin/python3
"""Module that defines a Student class with JSON serialization capability."""


class Student:
    """Represents a student with first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initializes a new Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns the dictionary representation of the instance
        for JSON serialization.
        """
        return self.__dict__
