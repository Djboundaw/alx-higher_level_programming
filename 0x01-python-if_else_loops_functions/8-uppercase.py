#!/usr/bin/python3
def uppercase(str):
    length = len(str)
    for i in range(length):
        if (ord(str[i]) > 96) and (ord(str[i]) < 123):
            letter = chr(ord(str[i]) - 32)
            print("{}".format(letter), end="")
        else:
            print("{}".format(str[i]), end="")
    print("")
