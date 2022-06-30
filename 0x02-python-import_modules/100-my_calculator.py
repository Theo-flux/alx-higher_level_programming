#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    size = len(argv) - 1
    if (size != 3):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>", end="\n")
        exit(1)
    else:
        operator = {'+':add, '-':sub, '*':mul, '/':div}
        a = int(argv[1])
        b = int(argv[3])
        if argv[2] in list(operator.keys()):
            print("{} {} {} = {:d}".format(argv[1], argv[2], argv[3], operator[argv[2]](a, b)), end="\n")
        else:
            print("Unknown operator. Available operators: +, -, * and /", end="\n")
            exit(1)

