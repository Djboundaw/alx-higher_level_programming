#!/usr/bin/python3
""" Function to read a text file """


def read_file(filename=""):
    """Print text to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
