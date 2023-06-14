#!/usr/bin/python3
"""Replace all occurence by another"""


def search_replace(my_list, search, replace):
    return list(map(lambda x: replace if x == search else x, my_list))
