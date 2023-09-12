#!/usr/bin/python3
class MyInt(int):
    """ myint class """
    def __init__(self, value):
        super().__init__()

    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
