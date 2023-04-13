#!/usr/bin/python3
""" Dictionary description for simple data structure """


def class_to_json(obj):
    """ Returns dico description of obj

    Args:
        obj: a python object
    """
    return obj.__dict__
