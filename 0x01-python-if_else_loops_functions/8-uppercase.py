#!/usr/bin/python3
def uppercase(str):
    uppercase_str = ""
    string = str
    for char in string:
        if 'a' <= char <= 'z':
            uppercase_char = chr(ord(string) & ~32)
        else:
            uppercase_char = char
        uppercase_str += uppercase_char
    print("{}".format(uppercase_str))
    return uppercase_str
