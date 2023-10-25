from game.resources import possible_words
import random

def setup():
    secret_word = possible_words[random.randint(0, len(possible_words))]
    underlined_word = []
    chances_left = 6

    for i in range(0, len(secret_word)):
        underlined_word += '_'

    return secret_word, underlined_word, chances_left


def update_underlined_word(guessed_letter, secret_word, underlined_word):
    for x in range(0, len(secret_word)):
        if guessed_letter in secret_word[x]:
            underlined_word[x] = guessed_letter

    return underlined_word