#!/usr/bin/python3
"""
Square class module
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """ square class """
    def __init__(self, size, x=0, y=0, id=None):
        """ init function """
        super().__init__(size, size, x, y, id)
        
    @property
    def size(self):
        """Size getter
        """
        return self.width

    @size.setter
    def size(self, value):
        """Size setter
        """

        # width not __width,
        # because you're calling width setter to set it to value

        self.width = value
        self.height = value

    def __str__(self):
        return(f"[Square] ({self.id}) {self.x}/{self.y} - {self.height}")
    
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
                self.size = args[1]
            elif (len(args) >= 3):
                self.x = args[2]
            elif (len(args) >= 4):
                self.y = args[3]
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
        dic["size"] = self.width
        dic["x"] = self.x
        dic["y"] = self.y
        return(dic)
