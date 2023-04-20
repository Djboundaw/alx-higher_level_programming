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

    def to_json_string(list_dictionaries):
        """ returns the json string representation of given argument

        Args:
            list_dictionaries (list): list of dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)
