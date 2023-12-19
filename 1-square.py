#!/usr/bin/python3
"""Defines a Square class."""


class Square:
    """Square class with a private instance attribute: size."""
    def __init__(self, size=0):
        """Initializes the square with a specific size.

        Args:
            size (int): Size of the square (default 0).
        """
        self.__size = size
