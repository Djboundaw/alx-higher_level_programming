#!/usr/bin/python3
""" Inheritance class of int """


class MyInt(int):
    """New subclass that inherits from int"""
    def __eq__(self, num):
        """Overriding == to !="""
        return self.real != num

    def __ne__(self, num):
        """Overriding != to =="""
        return self.real == num
