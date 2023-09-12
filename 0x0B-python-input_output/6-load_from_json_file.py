#!/usr/bin/python3
""" save josn """
import json


def load_from_json_file(filename):
    """ create object fron josn file """
    with open(filename, mode='r', encoding='UTF8') as f:
        json.load(f)
