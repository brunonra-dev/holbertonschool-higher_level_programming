#!/usr/bin/python3
"""
Student Class
"""


class Student:
    """
    attributes:
        - first_name
        - last_name
        - age
    """
    def __init__(self, first_name, last_name, age):
        first_name = first_name
        last_name = last_name
        age = age

    def to_json(self):
        return self.__dict__
