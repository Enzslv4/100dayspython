# hangman
from resources import possible_words, stages
import random
import os

print('Welcome to the hangman game!\n')


secret_word = possible_words[random.randint(0, len(possible_words))]
underlined_word = []
for i in range(0, len(secret_word)):
    underlined_word += '_'
chances_left = 6
print(secret_word)

while True:
    print(stages[chances_left])
    print('Your word is: ', *underlined_word)
    guessed_letter = input('Guess a letter: ').lower()
    if guessed_letter.isalpha():
        if guessed_letter in secret_word:
            for x in range(0, len(secret_word)):
                if guessed_letter in secret_word[x]:
                    underlined_word[x] = guessed_letter
            if '_' not in underlined_word:
                print(secret_word, 'You Win!!', sep='\n')
                break
            os.system('cls')
        else:
            chances_left -= 1
            os.system('cls')
            print('Wrong answer, Try again.')
            if chances_left == 0:
                print(stages[chances_left], 'Game over.', sep='\n')
                break
    else:
        print('Please type a letter, Try again.')


