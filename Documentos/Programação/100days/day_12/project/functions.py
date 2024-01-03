import vars
from os import system as clear_console


def game_logic(x):

    if x == 'e':
        chances_left = vars.EASY_LEVEL
    elif x == 'h':
        chances_left = vars.HARD_LEVEL

    while chances_left > 0:
        guess = int(input('Guess a number:\n'))
        if guess > vars.numb_to_guess:
            clear_console('cls')
            print('To High.')
            chances_left -= 1
        elif guess < vars.numb_to_guess:
            clear_console('cls')
            print('To Low.')
            chances_left -= 1
        elif guess == vars.numb_to_guess:
            clear_console('cls')
            print('You win! The number is:', vars.numb_to_guess)
            break
        print('Chances left:', chances_left)

    if chances_left == 0:
        print('You Lose!, the number was:', vars.numb_to_guess)