#!/usr/bin/python3
"""Print no c and C"""


def no_c(my_string):
    new_string = my_string.translate({ord(i): None for i in 'cC'})
    return new_string
