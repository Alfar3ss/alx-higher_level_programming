#!/usr/bin/python3
"""Defines a Square class."""


class Square:
    """Square class with private instance attribute: size."""
    def __init__(self, size=0):
        """Initializes the square with a specific size.

        Args:
            size (int): Size of the square (default 0).
        """
        self.__size = size  # Private instance attribute

        # Validate size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
