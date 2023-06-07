#!/usr/bin/python3
for decimal in range(0,99):
    hexadecimal = hex(decimal)
    message = "{} = {}"
    print(message.format(decimal, hexadecimal))
