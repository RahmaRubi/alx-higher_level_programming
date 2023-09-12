#!/usr/bin/python3
""" add attr to object if it possible to add """
def add_attribute(obj, attr, value):
    if hasattr(obj, '__dict__'):
        setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")
