#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new = dict(a_dictionary)
    for k, v in new.items():
        if(new[k] == value):
            del new[k]
    new = dict(new)
    return new
