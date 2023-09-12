#!/usr/bin/python3
"""adds items to list and saves it to file"""
import json
from sys import argv


if __name__ == '__main__':
    save = __import__('5-save_to_json_file').save_to_json_file
    load = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        x = load('add_item.json')
    except FileNotFoundError:
        x = []
    x.extend(argv[1:])
    save(x, 'add_item.json')
