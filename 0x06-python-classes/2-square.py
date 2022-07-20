#!/usr/bin/python3

"""class Square that defines a square"""

class Square:
    """Representation of a square"""
    def __init__(self, size = 0):
        """Initializes a new square"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("Size must be >= 0")
        self.__size = size
