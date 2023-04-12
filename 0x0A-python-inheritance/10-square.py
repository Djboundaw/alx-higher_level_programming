#!/usr/bin/python3
""" Creating a new class Square inheritance of Rectangle """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Creating a subclass of Rectangle"""
    def __init__(self, size):
        """initialization of subclass

        Args:
            size (int): size of the square
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
