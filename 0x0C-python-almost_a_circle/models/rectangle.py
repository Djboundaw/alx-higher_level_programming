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

    @property
    def width(self):
        """getter method for the arg width"""
        return self.__width

    @width.setter
    def width(self, width):
        """setter method for width"""
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be positive")
        self.__width = width


    @property
    def height(self):
        """getter method for height"""
        return self.__height

    @height.setter
    def height(self, height):
        """setter method for height"""
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be positive")
        self.__height = height

    
    @property
    def x(self):
        """"getter method for x"""
        return self.__x

    @x.setter
    def x(self, x):
        """setter method for x"""
        self.__x = x

    
    @property
    def y(self):
        """getter method for y"""
        return self.__y

    @y.setter
    def y(self, y):
        """setter method for y"""
        self.__y = y
