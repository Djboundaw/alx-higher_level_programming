#!/usr/bin/python3
""" Creating a class """


class Square:
    """It's a square"""
    def __init__(self, size=0):
        """Initializing
        Args:
            size (int): size of the square
        """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Initializing public instance method"""
        res = self.__size
        return (res * res)
