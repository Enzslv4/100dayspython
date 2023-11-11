from vars import *
import random
import os

def start_game():
    
    answer = input('Do you want to start the game? ')
    if answer == 'y':
        return True
    elif answer == 'n':
        return False
    else:
        return False
    
def game_logic():
    '''The logic of the game itself.'''

    score = 0

    def logic_hl(x, y):
        """Logic of High or Low, it checks if one is higher then the other based on your previews choice."""
        
        z = []
        z.append(x)
        z.append(y)
        
        if x[1] > y[1]:
            z.append(True)
        elif x[1] < y[1]:
            z.append(False)

        return z

    def picking_itens():
        x = random.choice(list(infos.items()))
        infos.pop(f'{x[0]}')
        return x
    
    thing_to_guess = picking_itens()
    thing_to_compare = picking_itens()

    while True:

        h_or_l = input(f'Your item is {thing_to_guess[0]}, is it "h"igher or "l"ower then {thing_to_compare[0]}? ').lower()

        if h_or_l == "h":
            os.system('cls')
            answer = logic_hl(thing_to_guess, thing_to_compare)
        elif h_or_l == 'l':
            os.system('cls')
            answer = logic_hl(thing_to_compare, thing_to_guess)
        
        if answer[2] == True:
            print(
                f'You guessed correctly! The "{answer[0][0]}" is searched {answer[0][1]} times, and {answer[1][0]}: {answer[1][1]} times.'
                )
            thing_to_guess = thing_to_compare
            if len(infos) > 0:
                thing_to_compare = picking_itens()
            else:
                print('You won everything! The score was:', score)
            score += 1
        else:
            print(
                f'You guessed wrong! The "{answer[0][0]}" is searched {answer[0][1]} times, and {answer[1][0]}: {answer[1][1]} times.'
                )
            print('Your score was', score)
            break

        