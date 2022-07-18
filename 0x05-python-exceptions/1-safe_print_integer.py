#!/usr/bin/python3
def safe_print_integer(value):
    if (value):
        try:
            print("{:d}".format(value), end="\n")
        except ValueError:
            return False
        else:
            return True
    else:
        return None
