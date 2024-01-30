#!/usr/bin/python3
""" module for welcome """



def say_my_name(first_name, last_name=""):
    """ function of welcome tested using doctest """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("my name is {} {}".format(first_name, last_name))

