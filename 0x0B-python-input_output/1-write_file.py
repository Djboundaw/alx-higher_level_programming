#!/usr/bin/python3
"""Function for to write string to a text file"""


def write_file(filename="", text=""):
    """Write a string to filename

    Args:
        filename: name of file
        text: string to write into file
    """
    with open(filename, 'w') as f:
        return f.write(text)
