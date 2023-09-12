#!/usr/bin/python3
""" write function """


def write_file(filename="", text=""):
    with open(filename, mode='w', encoding='UTF8') as f:
        return (f.write(text))
