#!/usr/bin/python3
"""
Class Base
"""


class Base:

    __nb_objects = 0

    def __init__(self, id=None):
        """Create Base

        Args:
            id (int, optional): Id of Base. Defaults to None.
        """
        if id == None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id