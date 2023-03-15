#!/usr/bin/python3
if __name__ == "__main__":
    """Program handling basic operations"""
    from calculator_1 import add, sub, mul, div
    import sys

    if (len(sys.argv) - 1) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    op = sys.argv[2]
    if op != '+' and op != '-' and op != '*' and op != '/':
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if op == '+':
        print("{} {} {} = {}".format(a, sys.argv[2], b, add(a, b)))
    elif op == '-':
        print("{} {} {} = {}".format(a, sys.argv[2], b, sub(a, b)))
    elif op == '*':
        print("{} {} {} = {}".format(a, sys.argv[2], b, mul(a, b)))
    else:
        print("{} {} {} = {}".format(a, sys.argv[2], b, div(a, b)))
