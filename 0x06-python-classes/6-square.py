#!/usr/bin/python3
""" Creating a class """


class Square:
    """It's a square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializing
        Args:
            size (int): size of the square
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """The getter of position"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """The setter of position"""
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """The area square"""
        res = self.__size
        return (res * res)

    def my_print(self):
        """Print the square with character #"""
        res = self.__size
        if res == 0:
            print("")
        else:
            for i in range(res):
                for j in range(res):
                    print("#", end="")
                print("")
