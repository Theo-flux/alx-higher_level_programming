#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    listLen = len(my_list)
    i = listLen - 1

    if (listLen != 0):
        while (i >= 0):
            print("{:d}".format(my_list[i]), end="\n")
            i = i - 1
