#!/usr/bin/python3
"""
Rectangle class module
"""


from models.base import Base


class Rectangle(Base):
    """ rectangle class inherits from base """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ constructor function with private attributes """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    @property
    def width(self):
        """ width getter """
        return(self.__width)
    
    @width.setter
    def width(self, value):
        """ width setter """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """ height getter """
        return(self.__height)

    @height.setter
    def height(self, value):
        """height setter """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """ x getter """
        return(self.__x)
    
    @x.setter
    def x(self, value):
        """ x setter """
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value
    
    @property
    def y(self):
        """ y getter """
        return(self.__y)

    @y.setter
    def y(self, value):
        """ y setter """
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value
    
    def area(self):
        """ area calc """
        return(self.__height * self.__width)

    def display(self):
        """ disply rec in hash """
        pattern = self.__width * "#"
        for i in range (self.__height):
            print(pattern)
    
    def __str__(self):
        """ overriding the str 
        str is a special function for print(obj)
        or print(str(obj)) gives message
        """
        return(f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}")

    def update(self, *args, **kwargs):
        """
        like the variadic function in c
        args is an array to accept different number of paramters
        kwargs is pointer of array for dictionary arguments like
        a=3, y= 4 returning a tuple (key, value)
        """
        if (args):
            if (len(args) >= 1 ):
                self.id = args[0]
            elif (len(args) >= 2):
                self.width = args[1]
            elif (len(args) >= 3):
                self.height = args[2]
            elif (len(args) >= 4):
                self.x = args[3]
            elif (len(args) >= 5):
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ dict method
            we couldn't use self.__dict__ directly because it returns the class name before the attr 
            like __Rectangle__x : 3 and the requred output is 'x': 3
            so instead, we 've created obj of the dict class and assined it manually
        """
        dic = dict()
        dic["id"] = self.id
        dic["width"] = self.width
        dic["height"] = self.height
        dic["x"] = self.x
        dic["y"] = self.y
        return(dic)

