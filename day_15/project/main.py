# coffe machine

from vars import *
from functions import start_machine, machine_logic
import os


while True:

    answer = start_machine()
    if answer == False:
        break
    else:
        os.system('cls')
        print(logo)

    print(resources['water'], resources['milk'], resources['coffee'])
    if (resources['water'] and resources['milk'] and resources['coffee']) > 0:
        print('Here is the menu:\n')

        for item in MENU.keys():
            cost = MENU[item]['cost']
            print(f'{item.capitalize()} costs: {cost}')


        choice = input('\nWhich type do you want? ("e"xpresso, "l"atte or "c"apuccino)\n')

        
        print('How do you wanna pay?\n')
        for i in coins_types.keys():
            coins = int(input(f"{i.capitalize()}({coins_types[i]} cents): "))
            amount += coins * coins_types[i]
        

        os.system('cls')
        print(logo)
        machine_logic(choice, amount)

    else:
        print('You ran out of resources!')