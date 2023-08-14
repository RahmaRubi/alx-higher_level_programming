#!/usr/bin/python3
#include "lists.h"
def print_reversed_list_integer(my_list=[]):
    if (my_list is None):
        print("", end="")
    else:
        for i in my_list:
            print("{:d}".format(int (my_list[-i])))
