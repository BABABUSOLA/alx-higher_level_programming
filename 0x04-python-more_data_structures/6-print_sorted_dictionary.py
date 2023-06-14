#!/usr/bin/python3
"""Return function that prints a dictionary by ordered key"""


def print_sorted_dictionary(a_dictionary):
    [print("{}: {}".format(k, a_dictionary[k])) for k in sorted(a_dictionary)]
