#!/usr/bin/python3
""" Creating a new class """


class BaseGeometry():
    """ BaseGeometry class """
    def __init__(self):
        """Initialize the class"""

    def area(self):
        """Public Instance method with exceptions raised"""
        raise Exception("area() is not implemented")
