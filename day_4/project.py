# ramdomized paper, scissors and rock

import random
import math

possibles_answers = [0, 1, 2]
answers_names = ['Rock', 'Paper', 'Scissors']
y = random.randint(0,2)

print('Welcome to the game paper, scissors and rock.')
print()
print('Please chose one of them:')
x = int(input('0 for Rock, 1 for Paper and 2 for Scissors: '))
module_subtraction = int(math.fabs(x - y))

if x in possibles_answers:
    print('You choose: ', answers_names[x])
    print('The computer answer is:', answers_names[y])
    if x == y:
        print('You Tied.')
    elif module_subtraction == 1:
        if x > y:
            print('You Win!')
        else:
            print('You Lose :(')
    else:
        if x == 0:
            print('You Win!')
        else:
            print('You Lose :(')
else:
    print('Wrong argument, please try again.')