#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        if type(size) is not int:
            raise Exception("size must be an integer")
        if size < 0:
            raise Exception("size must be >= 0")
        self.__size = size
