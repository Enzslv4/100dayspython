# guess the number game

import random
from functions import game_logic

print('Welcome to the Guessing Game!!\n')

level = input('Choose between "e"asy or "h"ard:\n')

game_logic(level)