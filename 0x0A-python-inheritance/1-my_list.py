#!/usr/bin/python3
""" module has a class inherit from list class """



class MyList(list):
    """
    class MyList that inherits from list
    """

    def print_sorted(self):
        """ function for printing sorted list """
        new_list = self.copy()
        new_list.sort()
        print(new_list)
