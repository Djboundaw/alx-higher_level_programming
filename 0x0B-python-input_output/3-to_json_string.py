#!/usr/bin/python3
"""Function that returns JSON representation of an object"""
import json
"""Importing json module"""


def to_json_string(my_obj):
    """Returns representation of my_obj

    Args:
        my_obj: object to returns it's JSON representation
    """
    return json.dumps(my_obj)
