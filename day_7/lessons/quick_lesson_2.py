import random

possible_words = ['agua', 'fogo', 'ar', 'terra']

secret_word = random.choice(possible_words)
print(secret_word)
guessed_letter = input('Guess a letter: ').lower()
underlined_word = []

for a in secret_word:
    underlined_word += '_'

for x in range(0, len(secret_word)):
    if guessed_letter in secret_word[x]:
        underlined_word[x] = guessed_letter

print(*underlined_word)