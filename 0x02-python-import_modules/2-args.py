#!/usr/bin/python3
from sys import argv
argv.pop(0)
argvLen = len(argv)
i = 0
if argvLen != 0:
    if (argvLen == 1):
        print("{:d} argument:".format(argvLen), end="\n")
    else:
        print("{:d} arguments:".format(argvLen), end="\n")
    while i < argvLen:
        print("{:d}: {}".format(i, argv[i]), end="\n")
        i = i + 1
else:
    print("{:d} arguments.".format(argvLen), end="\n")
