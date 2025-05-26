#!/usr/bin/python3
"""Defines a class MyList that inherits from list."""


class MyList(list):
    """A subclass of list that provides additional methods."""

    def print_sorted(self):
        """Prints the list in ascending sorted order.
        
        This method does not modify the original list, it just prints
        a sorted version of it. All elements must be of type int.
        """
        print(sorted(self))
