#!/usr/bin/python3
"""
Class Rectangle
"""

from models.base import Base


class Rectangle(Base):
    """the class Rectangle that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Init function

        Args:
            width (int): width of Rectangle
            height (int): height of Rectangle
            x (int, optional): x of Rectangle. Defaults to 0.
            y (int, optional): y of Rectangle. Defaults to 0.
            id (int, optional): id of Rectangle. Defaults to None.

        Raises:
            TypeError: width must be an integer
            TypeError: height must be an integer
            TypeError: x must be an integer
            TypeError: y must be an integer
            ValueError: width must be > 0
            TypeError: height must be > 0
            ValueError: x must be >= 0
            TypeError: y must be >= 0
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if height <= 0:
            raise TypeError("height must be > 0")
        if x < 0:
            raise ValueError("x must be >= 0")
        if y < 0:
            raise TypeError("y must be >= 0")
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    def __str__(self):
        return f'[Rectangle] ({self.id}) {self.__x}/{self.__y} - \
{self.__width}/{self.__height}'

    @property
    def width(self):
        """Return width of Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width of Rectangle"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Return height of Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height of Rectangle"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Return x of Rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set x of Rectangle"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be > 0")
        self.__x = value

    @property
    def y(self):
        """Return y of Rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set y of Rectangle"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be > 0")
        self.__y = value

    def area(self):
        """Return area of Rectangle"""
        return self.__width * self.__height

    def display(self):
        """Print Rectangle"""
        ret = ""
        if self.__width == 0 or self.__height == 0:
            return ""

        for posrow in range(self.__y):
            ret += "\n"
        for row in range(self.__height):
            for poscol in range(self.__x):
                ret += " "
            for col in range(self.__width):
                ret += "#"
            if row != self.__height - 1:
                ret += "\n"

        print(ret)

    def update(self, *args, **kwargs):
        """Set attributes of Rectangle"""
        attrs = ["id", "width", "height", "x", "y"]

        if args:
            for arg in range(len(args)):
                setattr(self, attrs[arg], args[arg])
        else:
            for k, v in kwargs.items():
                if k in attrs:
                    setattr(self, k, v)

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        return {"x": self.__x, "y": self.__y, "id": self.id,
                "height": self.__height, "width": self.__width}
