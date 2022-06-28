#!/usr/bin/python3
for i in range(0, 99, 1):
    if (i < 10):
        print("{} = 0x{}".format(i, i))
    elif(i > 9):
        if(i % 16 == 0):
           print("{} = 0x{:0.0f}0".format(i, i/16))
        elif(i % 16 > 9 and i % 16 < 16):
            if (i % 16 == 10):
                print("{} = 0x{}a".format(i, i/16))
            elif(i % 16 == 11):
                print("{} = 0x{}b".format(i, i/16))

