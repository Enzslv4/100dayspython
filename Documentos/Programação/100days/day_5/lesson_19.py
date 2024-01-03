# FizzBuzz

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print(number, 'FizzBuzz')
    elif number % 3 == 0:
        print(number, 'Fizz')
    elif number % 5 == 0:
        print(number, 'Buzz')
    else:
        print(number)