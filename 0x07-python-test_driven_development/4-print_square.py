#!/usr/bin/python3
"""
This is the 4-print_square.py module
"""

def print_square(size):
    """
    Function that prints a square with the character #.

    Raises:
        TypeError:
            - If size is not int
            - If size is float and less than 0
        ValueError:
            - If size < 0
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end='')
        print()
