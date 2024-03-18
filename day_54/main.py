import time

def calculate(function):
    time.sleep(2)
    function()

@calculate
def add():
    result = 2 + 1
    print(result)

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

#Functions are first-class objects, can be passed around as arguments e.g. int/string/float etc.

