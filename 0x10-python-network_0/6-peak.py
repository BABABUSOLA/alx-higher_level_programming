#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""

def find_peak(list_of_integers):
    """
    Args:
        list_of_integers(int): list of integers to find peak of
    Returns: peak of list_of_integers or None
    """

    if list_of_integers is None or list_of_integers == []:
        return None

    lo = 0
    hi = len(list_of_integers) - 1

    while lo < hi:
        mid = (lo + hi) // 2
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            lo = mid + 1
        else:
            hi = mid

    return list_of_integers[lo]
