#!/usr/bin/python3
""" class rectangle"""


class Rectangle:
    """ rectangle class"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ an instance method called when an object is created"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        """ special function returns strings """
        rectangle = ""
        if self.width == 0 or self.height == 0:
            return(rectangle)
        pattern = self.print_symbol * self.width
        for i in range(self.height):
            if i == self.height - 1:
                rectangle += pattern
                break
            rectangle += pattern + "\n"
        return(rectangle)

    def __repr__(self):
        """ special function returns some string used in eval as a code """
        return ("Rectangle({}, {})".format(self.width, self.height))

    def __del__(self):
        """ destructor function """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
