#!/usr/bin/python3
#from dis import dis
def magic_calculation(a,b):
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')

            result += ((b**a) / i)
        except Exception:
            result = b + a
            break
    return result

#dis(magic_calculation)
