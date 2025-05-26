#!/usr/bin/python3
"""
This module defines a class MyList that inherits from the built-in list class.
It includes a method that prints the list sorted in ascending order.
"""


class MyList(list):
    """
    MyList is a subclass of list.
    It provides a method to print the list in sorted ascending order
    without modifying the original list.
    """

    def print_sorted(self):
        """
        Prints the list elements in ascending order.
        The original list remains unchanged.
        """
        print(sorted(self))
