# hangman
from game.resources import stages
from game.hangman import setup, update_underlined_word
from utils.terminal import clear


print('Welcome to the hangman game!\n')

secret_word, underlined_word, chances_left = setup()
print(secret_word)

while True:
    print(stages[chances_left])
    print('Your word is: ', *underlined_word)

    if chances_left == 0:
        clear()
        print(stages[chances_left], 'Game over.', sep='\n')
        break

    if '_' not in underlined_word:
        print('You Win!!', sep='\n')
        break

    guessed_letter = input('Guess a letter: ').lower()
    if not guessed_letter.isalpha():
        clear()
        print('Please type a letter, Try again.')
        continue

    if guessed_letter in secret_word:
        underlined_word = update_underlined_word(guessed_letter, secret_word, underlined_word)
        clear()
        continue

    chances_left -= 1
    clear()
    print('Wrong answer, Try again.')


