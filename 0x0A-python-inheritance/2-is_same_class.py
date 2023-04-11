#!/usr/bin/python3
""" Instance of a class """


def is_same_class(obj, a_class):
    """Returns True if obj is an instance of a_class
        otherwise returns False
        Args:
            obj: the object to check
            a_class: a class object
    """
    if type(obj) == a_class:
        return True
    else:
        return False
