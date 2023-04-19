#!/usr/bin/python3
""" New class inherits from Base """
from models.base import Base


class Rectangle(Base):
    """Creating a new class Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """class constructor

        Args:
            width: width of the rectangle
            height: Height of the rectanlge
            x: initialized with 0
            y: initialized with 0
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def get_width(self):
        """getter method for the arg width"""
        return self.__width

    def set_width(self, width):
        """setter method for width"""
        self.__width = width

    def get_height(self):
        """getter method for height"""
        return self.__height

    def set_height(self, height):
        """setter method for height"""
        self.__height = height

    def get_x(self):
        """"getter method for x"""
        return self.__x

    def set_x(self, x):
        """setter method for x"""
        self.__x = x

    def get_y(self):
        """getter method for y"""
        return self.__y

    def set_y(self, y):
        """setter method for y"""
        self.__y = y
