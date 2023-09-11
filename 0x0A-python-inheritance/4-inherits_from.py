#!/usr/bin/python3
""" exactly a subclass """


def inherits_from(obj, a_class):
    """ function checks if the object is exactly a subclasss """
    if (isinstance(obj, a_class) and type(obj) != a_class):
        return (True)
    else:
        return (False)
