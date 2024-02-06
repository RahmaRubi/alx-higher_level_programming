#!/usr/bin/python3
""" reading module """


def read_file(filename=""):
    """ reading and printing function """
    with open(filename, 'r', encoding="utf-8") as f:
        content = f.read()
        print(content)
