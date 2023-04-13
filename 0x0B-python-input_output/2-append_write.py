#!/usr/bin/python3
"""Function that appends a string at the end"""


def append_write(filename="", text=""):
    """Append text to filename

    Args:
        filename: name of file
        text: string to append to the text file
    """
    with open(filename, 'a') as f:
        return f.write(text)
