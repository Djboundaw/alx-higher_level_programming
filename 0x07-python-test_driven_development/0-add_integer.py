#!/usr/bin/python3
def add_integer(a, b=98):
    """ Addition of two integers
    Args:
        @a: first argument
        @b: second argument
    """
    if not (isinstance(a, float) or isinstance(a, int)):
        raise TypeError("a must be an integer")
    elif not (isinstance(b, float) or isinstance(b, int)):
        raise TypeError("b must be an integer")
    else:
        a = int(a)
        b = int(b)
    return (a + b)
