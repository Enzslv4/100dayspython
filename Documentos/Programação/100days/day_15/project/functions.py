from vars import *
import random
import string

def start_machine():
    
    answer = input('Do you want to start the Coffe Machine? ')
    if answer == 'y':
        return True
    elif answer == 'n':
        return False
    else:
        return False
    
def machine_logic(choice, amount):

    for coffe_type in MENU.keys():

        if choice == coffe_type[0]:
            if amount >= MENU[coffe_type]['cost']:

                resources['water'] -= MENU[coffe_type]['ingredients']['water']
                resources['milk'] -= MENU[coffe_type]['ingredients']['milk']
                resources['coffee'] -= MENU[coffe_type]['ingredients']['coffee']


                print(f'Here is your {coffe_type.capitalize()}, enjoy!')

            else:
                print('Not enough money for this operation!')


