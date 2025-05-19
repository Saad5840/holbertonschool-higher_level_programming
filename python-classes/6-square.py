#!/usr/bin/python3
"""Defines a class Square with size and position."""


class Square:
    """Represents a square with size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square with optional size and position.

        Args:
            size (int): size of the square (default 0)
            position (tuple): tuple of 2 positive integers (default (0, 0))
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get the current position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square with validation."""
        if (
            not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(num, int) for num in value) or
            not all(num >= 0 for num in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current square area."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square with the character '#' to stdout.

        Uses position to offset printing:
        - position[1] is the number of newlines before the square
        - position[0] is the number of spaces before each line of the square
        If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print()
            return

        # Print empty lines for position[1]
        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            # Print spaces for position[0], then '#' * size
            print(" " * self.__position[0] + "#" * self.__size)
