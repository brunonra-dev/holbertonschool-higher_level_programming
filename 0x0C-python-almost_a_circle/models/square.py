#!/usr/bin/python3
"""
Class Square
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """the class Square that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Init function

        Args:
            size (int): size of Square.
            x (int, optional): x of Square. Defaults to 0.
            y (int, optional): y of Square. Defaults to 0.
            id (int, optional): id of Square. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f'[Square] ({self.id}) {self.x}/{self.y} - {self.width}'

    @property
    def size(self):
        """Return size of Rectangle"""
        return self.width

    @size.setter
    def size(self, size):
        """Set size of Rectangle"""
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """Set attributes of Rectangle"""
        attrs = ["id", "size", "x", "y"]
        if args:
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        else:
            for k, v in kwargs.items():
                if k in attrs:
                    setattr(self, k, v)

    def to_dictionary(self):
        """Returns the dictionary representation of a Square"""
        return {"id": self.id, "x": self.x, "size": self.size, "y": self.y}
