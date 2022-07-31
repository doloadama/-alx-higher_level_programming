#!/usr/bin/python3
# 0-add_integer.py

"""" A module to add two numbers
This module performs the addition operation between two numbers,
these numbers can be integers or floats.
"""


def add_integer(a, b=98):
    """Returns the integer addition of a and b
    """
if (type(a) is int or type(a) is float):
        if (type(b) is int or type(b) is float):
            return int(a) + int(b)
        else:
            raise TypeError("b must be an integer")
    else:
        raise TypeError("a must be an integer")
