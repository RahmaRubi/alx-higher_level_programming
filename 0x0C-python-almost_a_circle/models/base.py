#!/usr/bin/python3
""" bas class module """


import json


class Base:
    """ bas class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ constructor function """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    def to_json_string(list_dictionaries):
        """ converting data structure to string """
        return(json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """ saving data structure as a string in a seprate file """
        file_name = cls.__name__ + ".json"
        with open(file_name, 'w', encoding='utf-8') as f:
            if (list_objs is None):
                f.write("[]")
            else:
                list_dict = [obj.to_dictionary() for obj in list_objs]
                list_str = Base.to_json_string(list_dict)
                f.write(list_str)
            

