#!/usr/bin/python3
"""
Rectangle class
"""


BaseGeometry = __import__('9-rectangle').BaseGeometry


class Square(Rectangle):
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size ** 2

    def __str__(self):
        return(f"[Rectangle] {self.__size}/{self.__size}")
