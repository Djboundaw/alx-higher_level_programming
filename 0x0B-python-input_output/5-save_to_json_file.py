#!/usr/bin/python3
""" Writing an object to text file """
import json
"""Importing json"""


def save_to_json_file(my_obj, filename):
    """Using json representation,
    write content of my_obj to filename

    Args:
        my_obj: python object
        filename: where to write content of my_obj
    """
    my_str = json.dumps(my_obj)
    with open(filename, 'w') as f:
        return f.write(my_str)
