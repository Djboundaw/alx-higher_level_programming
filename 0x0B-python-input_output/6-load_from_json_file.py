#!/usr/bin/python3
""" Creating object from a json file """
import json
"""Importing json module"""


def load_from_json_file(filename):
    """Function will create a python object from a json file

    Args:
        filename: a json file
    """
    with open(filename) as f:
        return json.load(f)
