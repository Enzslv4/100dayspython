# auction program

from os import system
from art import logo

participants = {}

def winner_check(a):
    b = 0
    c = ''
    for name in a:
        if a[name] > b:
            b = a[name]
            c = name
    return c

print(logo)
while True:
    name = input('Who wants to enter the game:\n')
    bid = int(input('How much do you wanna risk?\n'))
    participants[name] = bid
    add_participant = input('Add another participant? ("Y"es or "N"o)\n').lower()
    if add_participant == 'y':
        system('cls')
        continue
    elif add_participant == 'n':
        system('cls')
        winner = winner_check(participants)
        print('The winner is', winner)
        break

    
