#!/usr/bin/python3


"""
Module for serializing and deserializing a custom object using pickle.
"""


import pickle


class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the object to the given filename using pickle.
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception:
            pass  # Fails silently as specified

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize and return an instance of CustomObject from the given filename.
        If the file is not valid or doesn't exist, return None.
        """
        try:
            with open(filename, 'rb') as f:
                obj = pickle.load(f)
                if isinstance(obj, cls):
                    return obj
        except Exception:
            return None
        return None
