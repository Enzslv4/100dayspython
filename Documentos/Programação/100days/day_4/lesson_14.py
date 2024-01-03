# name roulette

import random
import os

print('Name Roulette')
names_list = []
for i in range(0, 10):
    print(i)
    name = input('Type a name to be stored: ')
    names_list.append(name)
    i += 1

while True:
    print(names_list)
    answer = input('Do you need to choice randomly a name? ')
    if answer == 'y':
        print(random.choice(names_list))
    else:
        break

