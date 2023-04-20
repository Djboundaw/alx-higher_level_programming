#!/usr/bin/python3
""" An inheritance class from Rectangle """
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defining a new class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Print and str representation of square"""
        my_str = "[Square]"
        x = self.x
        y = self.y
        width = self.width
        return "{} ({}) {}/{} - {}".format(my_str, self.id, x, y, width)

    @property
    def size(self):
        """getter method for size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """setter for the size of a square"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value
