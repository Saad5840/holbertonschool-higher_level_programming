#!/usr/bin/env python3
"""Defines VerboseList class that extends list and prints notifications on modifications."""


class VerboseList(list):
    """List subclass that notifies on append, extend, remove, and pop operations."""

    def append(self, item):
        """Append item to the list and print a notification."""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """Extend list by appending elements from the iterable and print a notification."""
        count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{count}] items.")

    def remove(self, item):
        """Remove first occurrence of item and print a notification before removal."""
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=None):
        """Pop and return item at index (default last). Print notification before popping."""
        if index is None:
            index = -1
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
