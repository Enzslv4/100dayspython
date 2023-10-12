# password generator

import string
import random

print("Password Generetor\n")

numb_letters = int(input('How many letters do you want?\n'))
numb_simbols = int(input('How many simbols do you want?\n'))
numb_numbers = int(input('How many numbers do you want?\n'))
total_chars = numb_letters + numb_numbers + numb_simbols

a = 0
b = 0
c = 0
state = True
letters = string.ascii_letters
simbols = string.punctuation
password = ''

for d in range(0, total_chars):
    
    if state:
        ...
    else:
        d -= 1
        state = True
    
    rand_char = random.choice(letters)
    rand_simb = random.choice(simbols)
    rand_numb = random.randint(0,9)
    possible_char = [rand_char, rand_simb, rand_numb]
    i = random.randint(0,2)

    if i == 0:
        if a < numb_letters:
            password += str(possible_char[i])
            a += 1
        else:
            state = False
            continue
    elif i == 1:
        if b < numb_simbols:
            password += str(possible_char[i])
            b += 1
        else:
            state = False
            continue
    elif i == 2:
        if c < numb_numbers:
            password += str(possible_char[i])
            c += 1
        else:
            state = False
            continue
    

print(password)
    
