#!/usr/bin/python3
"""
BaseGeometry class
"""


class BaseGeometry:
    """
    Raises:
        - Exception: "area() is not implemented"
        - TypeError: must be an integer
        - ValueError: must be greater than 0
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")

    class Rectangle(BaseGeometry):
        """
        Class Rectangle that inherits from BaseGeometry
        """
        def __init__(self, width, height):
            self.__width = width
            self.__height = height
            self.integer_validator("width", width)
            self.integer_validator("height", height)
