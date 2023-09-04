#!/usr/bin/python3
class Rectangle:
    def __init__(self, width = 0, height = 0):
        self.__width = width
        self.__height = height
    
    @property
    def width(self):
        return(self.__width)
        
    @widthsetter
    def width(self, value):
        if value not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return(self.__height)

    @heightsetter
    def height(self, value):
        if value not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
