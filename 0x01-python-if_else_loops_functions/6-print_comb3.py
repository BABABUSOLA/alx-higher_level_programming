#!/usr/bin/python3
last_i = None
last_j = None
for i in range(10):
    for j in range(i+1, 10):
        last_i = i
        last_j = j
        if i == last_i and j == last_j-1:
            print("{:01d}{:01d}".format(i, j), end= (', '))
        else:
            print("{:01d}{:01d}".format(i, j), end=(' '))
