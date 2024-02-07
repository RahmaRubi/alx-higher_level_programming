#!/usr/bin/python3
""" deserializing module """


import json


def from_json_string(my_str):
    """
    deserializing json function;
    retrieving the origina; python structure from json representation
    """
    return(json.loads(my_str))
