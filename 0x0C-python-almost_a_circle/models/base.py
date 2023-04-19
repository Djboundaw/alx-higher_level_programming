#!/usr/bin/python3
""" Class Base """

class Base:
    """Creating a new class"""
    def __init__(self, id=None):
        """Class constructor

        Args:
            id (int): public instance attribute
        """
        if id != None:
            id = id
        else:
            __nb_objects++
            id = __nb_objects
