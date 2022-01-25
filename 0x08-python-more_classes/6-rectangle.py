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
        area: return area
        perimeter: return perimeter
    """
    number_of_instances = 0

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
        Rectangle.number_of_instances += 1

    def __str__(self):
        ret = ""
        if self.__width == 0 or self.__height == 0:
            return ""

        for i in range(self.__height):
            for j in range(self.__width):
                ret += "#"
            if i != self.__height - 1:
                ret += "\n"
        
        return ret

    def __repr__(self):
        return f'Rectangle({self.__width},{self.__height})'

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

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

    def area(self):
        """Return area of Rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Return perimeter of Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0

        return (self.__width + self.__height) * 2
