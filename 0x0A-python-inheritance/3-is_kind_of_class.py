#!/usr/bin/python3
""" Instance of a class or inherited classes"""


def is_kind_of_class(obj, a_class):
    """Returns True if obj is an instance of a_class
        otherwise returns False
        Using isinstance() instead of type()
        Args:
            obj: the object to check
            a_class: a class object
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
