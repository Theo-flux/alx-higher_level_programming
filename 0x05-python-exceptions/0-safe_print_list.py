#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if(my_list == []):
        return None
    else:
        try:
            i = 0
            lst = []
            while (i < x):
                print(my_list[i], end="")
                i = i + 1
            print("", end="\n")
        except IndexError as ex:
            pass
        finally:
            return(i)
