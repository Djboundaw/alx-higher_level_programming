#!/usr/bin/python3
""" Instance of a class and/or inherited classes"""


def inherits_from(obj, a_class):
    """Returns True if obj is an instance of subclass of a_class
        otherwise returns False
        Using isinstance() and type() for this function
        Args:
            obj: the object to check
            a_class: a class object
    """
    if isinstance(obj, a_class) and not type(obj) == a_class:
        return True
    else:
        return False
