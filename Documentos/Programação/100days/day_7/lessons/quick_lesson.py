import random

possible_words = ['agua', 'fogo', 'ar', 'terra']

secret_word = random.choice(possible_words)
print(secret_word)
guessed_letter = input('Guess a letter: ')

for letter in secret_word:
    if letter == guessed_letter:
        print('Right')
    else:
        print('Wrong')