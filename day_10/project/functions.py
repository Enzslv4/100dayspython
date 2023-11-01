def add(x, y):
    '''Add 2 numbers'''
    return x + y

def subtract(x, y):
    '''Subtract 2 numbers'''
    return x - y

def multiply(x, y):
    '''Multiply 2 numbers'''
    return x * y

def divide(x, y):
    '''Divide 2 numbers'''
    if y == 0:
        return print('Wrong arguments, try again.')
    else:
        return x / y

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}