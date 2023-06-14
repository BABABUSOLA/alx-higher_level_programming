#!/usr/bin/python3
"""Add the unique numbers"""


def uniq_add(my_list=[]):
    total = 0
    for i in list(set(my_list)):
        total = total + i
    return total
