#!/usr/bin/python3
from models.base import Base
""" import from base """


class Rectangle(Base):
    """ rectangle class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ init function """

        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        @property
        def width(self):
            """ getter/ setter for width """
            return(self.__width)

        @width.setter
        def width(self, value):
            if not isinstance(width, int):
                raise TypeError("width must be an intger")
            if width <= 0:
                raise ValueError("width must be > 0")
            self.__width = width

        @property
        def height(self):
            """ getter/ setter for height """
            return(self.__height)

        @height.setter
        def height(self, value):
            if not isinstance(height, int):
                raise TypeError("height must be an intger")
            if height <= 0:
                raise ValueError("height must be > 0")
            self.__height = height

        @property
        def x(self):
            """ getter/ setter for x """
            return(self.__x)

        @x.setter
        def x(self, value):
            if not isinstance(x, int):
                raise TypeError("x must be an intger")
            if x < 0:
                raise ValueError("x must be > 0")
            self.__x = x

        @property
        def y(self):
            """ getter/ setter for y """
            return(self.__y)

        @y.setter
        def y(self, value):
            if not isinstance(y, int):
                raise TypeError("y must be an intger")
            if y < 0:
                raise ValueError("y must be > 0")
            self.__y = y
