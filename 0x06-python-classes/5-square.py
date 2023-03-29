#!/usr/bin/python3
""" Creating a class """


class Square:
    """It's a square"""
    def __init__(self, size=0):
        """Initializing
        Args:
            size (int): size of the square
        """
        self.size = size

    @property
    def size(self):
        """the getter"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """The setter"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """The area square"""
        res = self.__size
        return (res * res)

    def my_print(self):
        """Print the square with character #"""
        res = self.__size
        for i in range(res):
            for j in range(res):
                print("#", end="")
            print("")
