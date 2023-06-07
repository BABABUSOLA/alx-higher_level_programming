#!/usr/bin/python3
def fizzbuzz():
    value = None
    for i in range(1, 101):
        if(i % 3 == 0 and i % 5 == 0):
           value  = "FizzBuzz"
        elif(i % 5 == 0):
           value = "Buzz"
        elif(i % 3 == 0):
           value  = "Fizz"
        else:
           value = i
        print(value, end=(' '))
