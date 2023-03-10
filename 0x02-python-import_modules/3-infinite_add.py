#!/usr/bin/python3
if __name__ == "__main__":
    """Program that adds all given args"""
    import sys

    num = len(sys.argv) - 1
    sum = 0
    if num == 0:
        sum = 0
    else:
        for i in range(1, num + 1):
            sum += int(sys.argv[i])
    print("{}".format(sum))
