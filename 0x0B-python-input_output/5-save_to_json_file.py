#!/usr/bin/python3
""" save josn """
import json


def save_to_json_file(my_obj, filename):
    """ write json into file """
    with open(filename, mode='r+', encoding='UTF8') as f:
        json.dump(my_obj, f)
