#!/usr/bin/python3
"""Replace the element of a list at a specific postion"""


def replace_in_list(my_list, idx, element):
    if idx < 0 | idx > len(my_list):
        return my_list
    else:
        my_list[i] = element
        return my_list
