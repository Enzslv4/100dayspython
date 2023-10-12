# ramdomized paper, scissors and rock

import os
import random
import math

possibles_answers = [0, 1, 2]
answers_names = ['Rock ✊', 'Paper ✋', 'Scissors ✌️']

print('Welcome to the game paper, scissors and rock.')
print()

score = 0

while True:
    print(f'The score is {score}/5 winnings.')
    print('Please chose one of them')
    x = int(input('0 for Rock, 1 for Paper and 2 for Scissors:\n'))
    y = random.randint(0,2)
    subtraction_module = int(math.fabs(x - y))
    if x in possibles_answers:
        print('You choose: ', answers_names[x])
        print('The computer answer is:', answers_names[y])
        if x == y:
            print('You Tied.')
        elif subtraction_module == 1:
            if x > y:
                score += 1
                print('You Win! 👏👏👏')
            else:
                score -= 1
                print('You Lose 😭')
        else:
            if x == 0:
                score += 1
                print('You Win! 👏👏👏')
            else:
                score -= 1
                print('You Lose 😭')
    else:
        print('Wrong argument.')
    if score < 0:
        score = 0
        print('\nGame over!\n')

    reset = input('Do you wanna try again?\n')
    if reset == 'y':
        if score == 5:
            print('Game Over, You Win! 👏👏👏')
            print(f'The score is {score}/5 of winnings.')
            break
        os.system('cls')
        continue
    else:
        print('You left the game 🚫.')
        break