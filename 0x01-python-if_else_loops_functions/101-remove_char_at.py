#!/usr/bash/python3
def remove_char_at(str, n):
    if (n > len(str)):
        return str
    else:
        str = str[:n]+str[n+1:]
        return str
