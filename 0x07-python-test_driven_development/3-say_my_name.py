#!/usr/bin/python3
"""
This is the 3-say_my_name.py module
"""

def say_my_name(first_name, last_name=""):
    """
    Function that prints My name is <first name> <last name>

    Raises:
        TypeError:
            - If first_name and last_name are not strings
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
