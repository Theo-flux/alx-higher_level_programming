#!/usr/bin/python3
def safe_print_division(a, b):
    if (a and b):
        result = 0
        try:
            result = a / b
        except ZeroDivisionError:
            result = None
            return result
        else:
            return result
        finally:
            print("Inside result: {}".format(result))
    else:
        return None
