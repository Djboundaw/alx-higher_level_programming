#!/usr/bin/python3
def add_integer(a, b=98):
    """ Addition of two integers
    Args:
        @a: first argument
        @b: second argument
    """
    if (a is None or a == "" or type(a) not in [int, float]):
        raise TypeError("a must be an integer")
    if (b is None or b == "" or type(b) not in [int, float]):
        raise TypeError("b must be an integer")
    else:
        a = int(a)
        b = int(b)
    return (a + b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
