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

    def update(self, *args, **kwargs):
        """Assigns arguments to attributes of square"""
        if args and len(args) != 0:
            self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
                self.height = args[1]
            elif len(args) > 2:
                self.x = args[2]
            elif len(args) > 3:
                self.y = args[3]
        elif not args and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size" and v:
                    self.size = v
                elif k == "x" and v:
                    self.x = v
                elif k == "y" and v:
                    self.y = v

    def to_dictionary(self):
        """Returns dictionary representation of square"""
        return {
                "id": self.id,
                "size": self.width,
                "x": self.x,
                "y": self.y
                }
