#!/usr/bin/python3
""" Writing in a file """


def append_after(filename="", search_string="", new_string=""):
    """Inserts new_string after each line
    of filename containing search_string

    Args:
        filename: file to open and write inside
        search_string: string to search for
        new_string: whast to insert after search_string
    """
    final_text = ""
    with open(filename, 'r') as f:
        for line in f:
            final_text += line
            if search_string in line:
                final_text += new_string
    with open(filename, 'w') as f:
        f.write(final_text)
