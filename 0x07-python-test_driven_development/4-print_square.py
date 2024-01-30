#!/usr/bin/python3
""" square module """


def print_square(size):
    """ square function """
    if (not isinstance(size, int)):
        raise TypeError("size must be an integer")
    elif (size < 0 ):
        raise ValueError("size must be >= 0")
    pattern = '#' * size
    for i in range(size):
        print(pattern)
