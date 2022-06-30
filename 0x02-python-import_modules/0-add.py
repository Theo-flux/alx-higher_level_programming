#!/usr/bin/python3
if __name__ == "__main__":
    """Print 1 + 2 = 3"""
    from add_0 import add
    
    a = 1
    b = 2
    res = add(a, b)
    print("{:d} + {:d} = {:d}".format(a,b,res), end="\n")
