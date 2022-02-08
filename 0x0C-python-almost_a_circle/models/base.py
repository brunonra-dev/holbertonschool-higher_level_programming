#!/usr/bin/python3
"""
Class Base
"""
import json
import os


class Base:
    """This class will be the “base” of all other classes"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Create Base

        Args:
            id (int, optional): Id of Base. Defaults to None.
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        with open(cls.__name__ + '.json', 'w', encoding='utf-8') as f:
            obj = []
            if list_objs:
                for item in list_objs:
                    obj.append(item.to_dictionary())

                return f.write(cls.to_json_string(obj))

            return f.write(cls.to_json_string(None))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string"""
        if json_string:
            return json.loads(json_string)
        return []

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if cls.__name__ == 'Rectangle':
            dummy = cls(2, 2)
        if cls.__name__ == 'Square':
            dummy = cls(2)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        if os.path.isfile(cls.__name__ + '.json') is False:
            return []

        with open(cls.__name__ + '.json', encoding='utf-8') as f:
            instance = []
            file = cls.from_json_string(f.read())

            for item in file:
                instance.append(cls.create(**item))

            return instance
