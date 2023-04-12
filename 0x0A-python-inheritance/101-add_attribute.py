#!/usr/bin/python3
""" Function that adds new attributes to an objects if possible """


def add_attribute(obj, att_name, value):
    """ To obj, add the attribute att_name

    Args:
        obj: an object
        att_name (str): new attribute for obj
        value: value of the attribute
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att_name, value)
