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
            raise ValueError("width must be > 0")
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
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """"getter method for x"""
        return self.__x

    @x.setter
    def x(self, x):
        """setter method for x"""
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """getter method for y"""
        return self.__y

    @y.setter
    def y(self, y):
        """setter method for y"""
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Public method
        returns area value of rectangle"""
        return self.__width * self.__height

    def display(self):
        """Public method
        Prints in stdout rectangle instance with the character #"""
        for k in range(self.__y):
            print()
        for i in range(self.__height):
            for e in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        x = self.__x
        y = self.__y
        Lon = self.__height
        lar = self.__width
        my_str = "[Rectangle]"
        return "{} ({}) {}/{} - {}/{}".format(my_str, self.id, x, y, lar, Lon)

    def update(self, *argv):
        """Public method
        assigns an argument to attributes"""
        self.id = argv[0]
        if len(argv) > 1:
            self.__width = argv[1]
        if len(argv) > 2:
            self.__height = argv[2]
        if len(argv) > 3:
            self.__x = argv[3]
        if len(argv) > 4:
            self.__y = argv[4]
