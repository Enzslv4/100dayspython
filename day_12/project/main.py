# guess the number game

import random
from functions import game_logic
from art import logo

print(logo)
print('Welcome to the Guessing Game!!\n')

level = input('Choose between "e"asy or "h"ard:\n')

game_logic(level)