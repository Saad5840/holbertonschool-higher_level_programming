#!/usr/bin/env python3
"""Defines CountedIterator class that counts items iterated over."""

class CountedIterator:
    """Iterator wrapper that counts how many items have been iterated."""

    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        item = next(self.iterator)  # may raise StopIteration naturally
        self.count += 1
        return item

    def get_count(self):
        """Return the number of items iterated so far."""
        return self.count
