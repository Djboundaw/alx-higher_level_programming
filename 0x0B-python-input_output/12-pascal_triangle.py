#!/usr/bin/python3
""" Pascal triangle """


def pascal_triangle(n):
    """Returns list of lists of integers

    Args:
        n (int): the max
    """
    if n <= 0:
        return []

    my_list = [[1]]
    while len(my_list) != n:
        first_ele = [1]
        lines = my_list[-1]
        for i in range(len(lines) - 1):
            first_ele.append(lines[i] + lines[i + 1])
        first_ele.append(1)
        my_list.append(first_ele)
    return my_list
