#!/usr/bin/python3
""" Lookup function """

def lookup(obj):
    """Returns list of available attributes
        and methods of an object"""
    my_list = dir(obj)
    return (my_list)
