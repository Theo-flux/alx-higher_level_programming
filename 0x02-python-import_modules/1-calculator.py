#!/usr/bin/python3
if __name__ = "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    res= 0
    res = add(a, b)
    print("{:d} + {:d} = {:d}".format(a, b, res), end="\n")
    res = sub(a, b)
    print("{:d} - {:d} = {:d}".format(a, b, res), end="\n")
    res = mul(a, b)
    print("{:d} * {:d} = {:d}".format(a, b, res), end="\n")
    res = div(a, b)
    print("{:d} / {:d} = {:d}".format(a, b, res), end="\n")
