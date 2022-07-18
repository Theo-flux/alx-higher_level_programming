#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    if (my_list and x):
        try:
            i = 0
            while i < x:
                if (type(my_list[i]) == int):
                    print("{:d}".format(my_list[i]), end="")
                else:
                    continue
                i = i + 1
            print("", end="\n")
        except IndexError:
            print(IndexError)
        else:
            return (i)
    else:
        return None
