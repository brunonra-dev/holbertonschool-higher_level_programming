#!/usr/bin/python3
"""Square module
Task of 0x06. Python - Classes and Objects

"""


class Square:
    """Description of Square Class

    Attributes:
        __size (int): size of square
        __position (tuple): position of Square

    Returns:
        area: return area of Square

    """

    def __init__(self, size=0, position=(0, 0)):
        """
        size (int): size of square

        Args:
            __size (int): size of square
            __position (tuple): position of Square

        Raises:
            TypeError: If size is not int or tuple ar not 2 positive integers.
            ValueError: If size < 0.


        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if (not isinstance(position, type((int, int)))):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (position[0] < 0 or position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__size = size
        self.__position = position

    @property
    def size(self):
        """return size of Square"""

        return(self.__size)

    @size.setter
    def size(self, size=0):
        """set size of Square"""

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    @property
    def position(self):
        """returns position of square"""

        return(self.__position)

    @position.setter
    def position(self, value):
        """sets position of square"""

        if (not isinstance(position, type((int, int)))):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (position[0] < 0 or position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = position

    def area(self):
        """return area of Square"""

        return (self.__size**2)

    def my_print(self):
        """print Square if size > 0"""
        if self.__size > 0:
            for row in range(self.__size):
                for pos in range(self.__position[0]):
                    print(" ", end='')
                for col in range(self.__size):
                    print("#", end="")
                print("")
        else:
            print("")
