#!/usr/bin/python3
""" class rectangle"""


class Rectangle:
    """ rectangle class"""
    def __init__(self, width=0, height=0):
        """ an instance method called when an object is created"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """ width getter/setter function """
        return(self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ height gettter setter function"""
        return(self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
