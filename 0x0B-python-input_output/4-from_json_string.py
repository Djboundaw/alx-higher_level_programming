#!/usr/bin/python3
""" Function that returns an object represented by a json string """
import json
"""Importing json"""


def from_json_string(my_str):
    """Return object represented by my_str

    Args:
        my_str: json string
    """
    return json.loads(my_str)
