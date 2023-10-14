# password generator

import string
import random

print("Password Generetor\n")

numb_letters = int(input('How many letters do you want?\n'))
numb_simbols = int(input('How many simbols do you want?\n'))
numb_numbers = int(input('How many numbers do you want?\n'))
total_chars = numb_letters + numb_numbers + numb_simbols

letters = string.ascii_letters
simbols = string.punctuation
normal_password = []
final_password = ''

for char in range(0, numb_letters):
    normal_password += random.choice(letters)

for char in range(0, numb_numbers):
    normal_password += str(random.randint(0,9))


for char in range(0, numb_simbols):
    normal_password += random.choice(simbols)

i = 0
while True:
    i = random.randint(0, len(normal_password) - 1)
    lenth = len(normal_password)
    final_password += normal_password[i]
    normal_password.pop(i)
    lenth -= 1
    if lenth == 0:
        break

print("You password is", final_password)

# random.shuffle(x) - this is a way more simple way to do the same as i did above