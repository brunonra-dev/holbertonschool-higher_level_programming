#!/usr/bin/python3
"""
MyList classes
"""

class MyList(list):
    """
    prints the list, but sorted (ascending sort)
    """
    def print_sorted(self):
        for item in self:
            if type(item) != int:
                raise TypeError

        print(sorted(self))