#!/usr/bin/python3
""" my list """


class MyList(list):
    """ class inherits from list class """
    def __init__(self):
        super().__init__()

    def print_sorted(self):
        x = sorted(self)
        print(x)
