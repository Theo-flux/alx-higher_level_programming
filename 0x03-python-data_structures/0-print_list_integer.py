#!/usr/bin/python3
def print_list_integer(my_list=[]):
    listLen = len(my_list)

    if (listLen != 0):
        for el in my_list:
            print("{:d}".format(el), end="\n")

