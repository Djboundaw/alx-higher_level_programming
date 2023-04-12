#!/usr/bin/python3
""" Creating a new class inheritance of BaseGeometry """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Creating a subclass of BaseGoemetry"""
    def __init__(self, width, height):
        """initialization of subclass

        Args:
            width (int): width of parameter
            height (int): height of the parameter
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
