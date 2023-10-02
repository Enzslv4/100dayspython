# odd or even

number = int(input('Digit a number: '))

try:
    if (number % 2) == 0:
        print('Odd.')
    else:
        print('Even.')
except ZeroDivisionError:
    print("U can't divide by zero.")