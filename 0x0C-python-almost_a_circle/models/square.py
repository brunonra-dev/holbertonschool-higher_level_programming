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
