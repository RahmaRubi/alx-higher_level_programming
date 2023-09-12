#!/usr/bin/python3
""" append fun """


def append_write(filename="", text=""):
    """ function appending text at the end """

    with open(filename, mode='a', encoding='UTF8') as f:
        return(f.write(text))
