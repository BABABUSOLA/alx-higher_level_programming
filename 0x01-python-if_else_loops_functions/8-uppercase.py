#!/usr/bin/python3
def uppercase(str):
    uppercase_str = ""
    for char in str:
        if 'a' <= char <= 'z':
            uppercase_char = chr(ord(str) & ~32)
        else:
            uppercase_char = char
        uppercase_str += uppercase_char
    print("{}".format(uppercase_str))
    return uppercase_str
