#!/usr/bin/python3
"""Replace the element of a list at a specific postion"""


def new_in_list(my_list, idx, element):
    new_list = my_list.copy()
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    else:
        new_list[idx] = element
        return new_list
