#!/usr/bin/python3
for n in range(10):
    for m in range(10):
        if n >= m:
            continue
        if n == 8 and m == 9:
            print("{}{}".format(n, m))
            break
        print("{}{}".format(n, m), end=", ")
