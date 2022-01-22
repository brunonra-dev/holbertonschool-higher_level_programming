#!/usr/bin/python3
"""
This is the 0-add_integer.py module
Raises:
    TypeError: if a and b are not integers or floats.
"""

def add_integer(a, b=98):
    """
    Return (int): the addition of a and b.
    """

    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)


