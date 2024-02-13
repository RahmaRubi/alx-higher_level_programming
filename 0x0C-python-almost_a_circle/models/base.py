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

    def from_json_string(json_string):
        """ converting the json string json_string to its original 
        data structure which is a list of dict
        """
        if json_string is None or "":
            return("[]")
        return(json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """that returns an instance with all attributes already set
        """
        obj = cls(1, 1)
        if dictionary:
            obj.update(**dictionary)
        return (obj)
            
    
    @classmethod
    def load_from_file(cls):
        """
        returns a list of instances
        """
        filename = f"{cls.__name__}.json"

        try:
            with open(filename, 'r') as file:
                json_data = file.read()
        except FileNotFoundError:
            return []

        json_rep_list = cls.from_json_string(json_data)
        newlist = list()
        for dic in json_rep_list:
            obj = cls.create(**dic)
            # astreisk for **dictionary in function def
            newlist.append(obj)
        return newlist
