#!/usr/bin/python3
""" addition module """


def add_integer(a, b=98):
    """ function adding two numbers with doctest file """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    elif (not isinstance(b, (int, float))):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)
    return(a + b)
