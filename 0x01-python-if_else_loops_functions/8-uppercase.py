#!/usr/bin/python3
def uppercase(str):
    uppercase_str = ""
    for char in str:
        uppercase_char = chr(ord(str) & ~32)
        uppercase_str += uppercase_char
    print("{}".format(uppercase_str))
    return uppercase_str
