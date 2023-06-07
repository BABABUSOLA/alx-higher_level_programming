#!/usr/bin/python3
def fizzbuzz():
    value = None
    for i in range(1, 101):
        if(i % 3):
           value  = "Fizz"
        elif(i % 5):
           value = "Buzz"
        elif(i % 3 and i % 5):
           value  = "FizzBuzz"
        else:
            value = i
    print(value, end=(''))
    return value
