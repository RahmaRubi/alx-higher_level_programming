#!/usr/bin/python3
""" module for printing a text """


def text_indentation(text):
    """ function """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for ch in text:
        print(ch, end="")
        if ch == '?' or ch == '.' or ch == ':':
            print("\n")
            ch = ch + 1
