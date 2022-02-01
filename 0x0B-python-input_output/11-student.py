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
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        dic = {}
        for key in attrs:
            if key in self.__dict__:
                dic[key] = self.__dict__[key]
        return dic

    def reload_from_json(self, json):
        for i in json:
            self.__dict__[i] = json[i]
