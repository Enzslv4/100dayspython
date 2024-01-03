# high or low game

from art import logo
from functions import *
from vars import *

print(logo)
print('Welcome to the High or Low Game!\n')

while True:

    answer = start_game()
    if answer == False:
        break

    game_logic()