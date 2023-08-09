#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if ((str.isupper(char))):
            print("{}".format(char))
        print("{:s}".format(char-32))
