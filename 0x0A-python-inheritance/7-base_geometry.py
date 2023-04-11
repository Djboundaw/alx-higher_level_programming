#!/usr/bin/python3
""" Creating a new class """


class BaseGeometry():
    """ BaseGeometry class """
    def __init__(self):
        """Initialize the class"""

    def area(self):
        """Public Instance method with exceptions raised"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Public Instance method - validates value

        Args:
            name (str): parameter's name
            value (int): parameter's value
        """
        if not type(value) == int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
