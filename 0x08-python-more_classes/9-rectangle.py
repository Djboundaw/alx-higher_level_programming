#!/usr/bin/python3
""" Creating a class """


class Rectangle:
    """class name Rectangle"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Instantiation with (0, 0)
        Args:
            width (int)
            height (int)
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    @classmethod
    def square(cls, size=0):
        """Return a square"""
        return (cls(size, size))

    def __str__(self):
        """Represents the rectangle with the character #"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        my_rectangle = []
        a = self.__width
        b = self.__height

        for i in range(b):
            [my_rectangle.append(str(self.print_symbol)) for j in range(a)]
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

    def __del__(self):
        """Instance deletion"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area():
            return (rect_1)
        elif rect_1.area() > rect_2.area():
            return (rect_1)
        else:
            return (rect_2)
