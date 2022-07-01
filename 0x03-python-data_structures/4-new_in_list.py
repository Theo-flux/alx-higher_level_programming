#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    listLen = len(my_list)

    if(listLen != 0):
        if (idx < 0 or idx > listLen - 1):
            return my_list
        else:
            new_list = my_list[:-1]
            new_list[idx] = element
            return new_list
