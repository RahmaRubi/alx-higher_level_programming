#!/usr/bin/python3
""" hash """
from models.base import Base
""" import from base """


class Rectangle(Base):
    """ rectangle class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ init function """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ getter/ setter for width """
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ getter/ setter for height """
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ getter/ setter for x """
        return (self.__x)

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ getter/ setter for y """
        return (self.__y)

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ area of the rectangle """
        return (self.__width * self.__height)

    def display(self):
        """ disply rectangle represented by # """
        rect = ""
        symbol = "#"
        pattern = symbol * self.width
        for j in range(self.__height):
            print(pattern)

    def __str__(self):
        """ a dunder function called implicitly when printing the object """
        return "[Rectangle] ({}) {}/{} - {}/{}".format
        (self.id, self.__x, self.__y, self.__width, self.__height)
