#!/usr/bin/python3
""" appending  module """


def append_write(filename="", text=""):
    """appending and printing no charcters function """
    with open(filename, 'a+', encoding="utf-8") as f:
        return(f.write(text))
