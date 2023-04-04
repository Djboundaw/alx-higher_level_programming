#!/usr/bin/python3
""" Creating a class """


class Rectangle:
    """class name Rectangle"""
    def __init__(self, width=0, height=0):
        """Instantiation with (0, 0)
        Args:
            width (int)
            height (int)
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """The getter of Rectangle's width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Setting the width's value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """The getter of the Rectangle's height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Setting the height's value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        a = self.__width
        b = self.__height
        return ((a + b) * 2)

    def __str__(self):
        """Represents the rectangle with the character #"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        my_rectangle = []
        a = self.__width
        b = self.__height

        for i in range(b):
            [my_rectangle.append("#") for j in range(a)]
            if i != (b - 1):
                my_rectangle.append("\n")
        return ("".join(my_rectangle))

    def __repr__(self):
        """Returns a string representation of the rectangle"""
        a = self.__width
        b = self.__height
        if a == 0 or b == 0:
            return ("")
        return ("Rectangle(" + str(a) + ", " + str(b) + ")")
