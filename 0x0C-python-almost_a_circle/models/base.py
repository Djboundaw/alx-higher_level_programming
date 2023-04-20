#!/usr/bin/python3
""" Class Base """
import json


class Base:
    """Creating a new class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor

        Args:
            id (int): public instance attribute
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the json string representation of given argument

        Args:
            list_dictionaries (list): list of dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file:

        Args:
            cls (class): child of class Base
            list_objs (list): list of instances
        """
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dicts = [ele.to_dictionary() for ele in list_objs]
                f.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list of the json string representation """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new_base = cls(2, 2)
            else:
                new_base = cls(2)
            new_base.update(**dictionary)
            return new_base

    @classmethod
    def load_from_file(cls):
        """Returns a list of instance"""
        filename = str(cls.__name__) + ".json"
        if not filename:
            return []
        with open(filename, 'r') as f:
            base_dicts = Base.from_json_string(f.read())
            return [cls.create(**dict) for dict in base_dicts]
