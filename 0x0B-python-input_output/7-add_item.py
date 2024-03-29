#!/usr/bin/python3
"""Adding arguments to a python list and save them to a file"""
import sys


if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    loadFromJsonFile = __import__('6-load_from_json_file').load_from_json_file

    try:
        objects = loadFromJsonFile("add_item.json")
    except FileNotFoundError:
        objects = []
    objects.extend(sys.argv[1:])
    save_to_json_file(objects, "add_item.json")
