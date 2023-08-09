#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if (not (str.isupper(char))):
            pass

        print("{:s}".format(char+32))
