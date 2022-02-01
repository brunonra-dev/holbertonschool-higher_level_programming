#!/usr/bin/python3
"""
Rectangle Class - define a rectangle
"""


class Rectangle:
    """
    Description of Rectangle Class

    Attributes:
        __w (int): width of Rectangle
        __h (int): height of Rectangle

    Raises:
        TypeError:
            - If width & height are not integer
        ValueError:
            - If width & height are not >= 0

    Returns:
        width: return width
        height: return height
    """

    def check(self, value=0, item=""):
        """Check errors"""
        if type(value) is not int:
            raise TypeError(item + " must be an integer")
        if value < 0:
            raise ValueError(item + " must be >= 0")

    def __init__(self, width=0, height=0):
        """init method"""
        self.check(width, "width")
        self.check(height, "height")
        self.height = height
        self.width = width

    @property
    def width(self):
        """Return width of Rectangle"""
        return(self.__width)

    @width.setter
    def width(self, value):
        """Set width of Rectangle"""
        self.check(value, "width")
        self.__width = value

    @property
    def height(self):
        """Return height of Rectangle"""
        return(self.__height)

    @height.setter
    def height(self, value):
        """Set height of Rectangle"""
        self.check(value, "height")
        self.__height = value