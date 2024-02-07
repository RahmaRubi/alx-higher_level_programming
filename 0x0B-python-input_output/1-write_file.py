#!/usr/bin/python3
""" writing  module """


def write_file(filename="", text=""):
    """ writing and printing no charcters function """
    with open(filename, 'w+', encoding="utf-8") as f:
        return(f.write(text))
