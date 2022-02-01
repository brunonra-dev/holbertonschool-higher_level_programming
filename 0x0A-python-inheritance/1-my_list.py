#!/usr/bin/python3
"""
MyList classes
"""


class MyList(list):
    """
    prints the list, but sorted (ascending sort)
    """
    def print_sorted(self):
        print(sorted(self))
