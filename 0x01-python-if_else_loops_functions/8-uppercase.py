#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if ((str.islower(char))):
            print("{:s}".format(ord(char)-32))
        print("{}".format(char))
