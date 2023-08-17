#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    new = set(my_list)
    for unique in new:
        sum += unique
    return (sum)
