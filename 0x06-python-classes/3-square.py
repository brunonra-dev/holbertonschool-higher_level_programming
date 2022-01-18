#!/usr/bin/python3
"""Square module
Task of 0x06. Python - Classes and Objects

"""


class Square:
    """Description of Square Class

    Attributes:
        __size (int): size of square

    """

    def __init__(self, size=0):
        """
        size (int): size of square

        Args:
            size: size of square

        Raises:
            TypeError: If size is not int.
            ValueError: If size < 0.

        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """
        Return area of Square

        """

        return (self.__size**2)
