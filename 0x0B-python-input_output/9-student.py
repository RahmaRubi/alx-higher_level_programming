#!/usr/bin/python3
""" student class """


class Student:
    """ student class """

    def  __init__(self, first_name, last_name, age):
        self.first_name = name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """defines function"""

        return self.__dict__


