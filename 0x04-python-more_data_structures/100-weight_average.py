#!/usr/bin/python3
def weight_average(my_list=[]):
    q = 0
    p = 0
    res = 0
    if my_list == []:
        return (0)
    for (x, y) in my_list:
        p += x * y
        q += y
    res = p / q
    return (res)
