#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    if abs(number) % 10 == 0:
        print("Last digit of {} is ".format(number), end="")
        print("{} and is 0".format(abs(number) % 10))
    elif abs(number) % 10 > 5:
        print("Last digit of {} is ".format(number), end="")
        print("{} and is greater than 5".format(abs(number) % 10))
    elif abs(number) % 10 < 6 and abs(number) % 10 != 0:
        print("Last digit of {} is ".format(number), end="")
        print("{} and is less than 6 and not 0".format(abs(number) % 10))
else:
    if abs(number) % 10 == 0:
        print("Last digit of {} is ".format(number), end="")
        print("{} and is 0".format(abs(number) % 10))
    else:
        print("Last digit of {} is -".format(number), end="")
        print("{} and is less than 6 and not 0".format(abs(number) % 10))
