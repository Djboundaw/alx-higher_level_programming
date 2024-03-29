#!/usr/bin/python3
def print_square(size):
    """ Prints a square with the character #
    Args:
        size: length of the square must be integer
    """
    if (not isinstance(size, int) or
            (isinstance(size, float) and size < 0)):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")

if __name__ == "__main__":
    import doctest
    doctest.testfile("./tests/4-print_square.txt")
