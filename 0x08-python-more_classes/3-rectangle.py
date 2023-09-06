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
        """ height gettter/setter function"""
        return(self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ area getter """
        return (self.__width) * (self.__height)

    def perimeter(self):
        """ perimeter getter """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width + self.__height)*2)

    def __str__(self):
        """ function returns strings """
        rectangle = ""
        if self.width == 0 or self.height == 0:
            return(rectangle)
        pattern = "#" * self.width
        for i in range(self.height):
            rectangle += pattern + "\n"
            if i == self.height - 1:
                rectangle += pattern
        return(rectangle)
