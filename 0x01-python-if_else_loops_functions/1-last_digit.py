#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = int(number % 10) if number >= 0 else int(-(-number % 10))
s="Last digit of {:d} is {:d}".format(number, last_digit)

if(last_digit == 0):
    print("{} and is 0".format(s))
elif(last_digit < 6 and last_digit > 0):
    print("{} and is less than 6 and not 0".format(s))
else:
    print("{} and is greater than 5".format(s))
