#!/usr/bin/python3
""" Creating a new class inheritance of BaseGeometry """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(BaseGeometry):
    """ Creating a subclass of BaseGoemetry"""
    def __init__(self, size):
        """initialization of subclass

        Args:
            width (int): width of parameter
            height (int): height of the parameter
        """
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """Will print width/height"""
        return ("[Rectangle] {}/{}".format(self.__size, self.__size))

    def area(self):
        """ The area of Square """
        return (self.__size * self.__size)
