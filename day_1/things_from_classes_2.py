# counting strings

import os

while True:
    name = input('Your name: ')
    try:
        type(int(name)) == True # i know that there is a better way to do this
        # but i just forgot how to kkkk
        print('Invalid argument')
        os.system('cls')
    except ValueError:
        print(f'Your name has {len(name)} letters.')
        break
