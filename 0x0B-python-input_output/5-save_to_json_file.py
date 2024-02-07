#!/usr/bin/python3
""" writing object module """


import json


def save_to_json_file(my_obj, filename):
    """ writing obj to a text_file function """
    with open(filename, 'w+', encoding="UTF-8") as f:
        f.write(json.dumps(my_obj))
