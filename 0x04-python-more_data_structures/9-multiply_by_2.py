#!/usr/bin/python3
"""REturn a new dictionary with all values multiplied by 2"""


def multiply_by_2(a_dictionary):
    return {x: y * 2 for x, y in a_dictionary.items()}
