# calculator

from functions import operations
from os import system
from art import logo

print(logo, 'Welcome to the calculator!\n')

while True:
    num1 = int(input('1° number:\n'))
    num2 = int(input('2° number:\n'))

    for i in operations:
        print(i)

    operation_symbol = input('Digit your operation symbol:\n')
    result = operations[operation_symbol](num1, num2)
    system('cls')
    print(f'The result of {num1} {operation_symbol} {num2} is', result)

    to_continue = 'y'

    while to_continue == 'y':
            to_continue = input('Do u want to continue?("y"es or "n"o)\n').lower()
            if to_continue == 'n':
                break
            num2 = int(input('2° number:\n'))
            operation_symbol = input('Digit your operation symbol:\n')
            other_result = operations[operation_symbol](result, num2)
            system('cls')
            print(f'The result of {result} {operation_symbol} {num2} is', other_result)

    if to_continue == 'n':
        break