#!/usr/bin/python3
"""Print a tuple with the length of a string and its first character"""


def multiple_returns(sentence):
    if len(sentence) == 0:
        my_turple = 0, None
    else:
        my_turple = len(sentence), sentence[0]
    return my_turple
