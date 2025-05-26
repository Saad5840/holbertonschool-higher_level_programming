#!/usr/bin/python3
"""
This module defines a class MyList that inherits from list.
It adds a method to print the list in sorted (ascending) order.
"""


class MyList(list):
    """
    MyList inherits from the built-in list class.
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order (without modifying the original list).
        """
        print(sorted(self))
