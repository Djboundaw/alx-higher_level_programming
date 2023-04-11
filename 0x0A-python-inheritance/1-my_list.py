#!/usr/bin/python3
""" Class inheritance of object list"""


class MyList(list):
    """Defining a class MyList that inherits from list"""
    def __init__(self):
        """ Object initialization """
        list.__init__(self)

    def print_sorted(self):
        """Public instance method
        Args:
            self"""
        print(sorted(self))
