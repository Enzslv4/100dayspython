# hangman

import random
import os

print('Welcome to the hangman game!\n')

possible_words = [
    'abruptly', 'absurd', 'abyss', 'affix', 'askew', 'avenue', 
    'awkward', 'axiom', 'azure', 'bagpipes', 'bandwagon', 'banjo', 
    'bayou', 'beekeeper', 'bikini', 'blitz', 'blizzard', 'boggle', 
    'bookworm', 'boxcar', 'boxful', 'buckaroo', 'buffalo', 'buffoon',
    'buxom', 'buzzard', 'buzzing', 'buzzwords', 'caliph', 'cobweb', 'cockiness',
    'croquet', 'crypt', 'curacao', 'cycle', 'daiquiri', 'dirndl', 'disavow',
    'dizzying', 'duplex', 'dwarves', 'embezzle', 'equip', 'espionage',
    'euouae', 'exodus', 'faking', 'fishhook', 'fixable', 'fjord',
    'flapjack', 'flopping', 'fluffiness', 'flyby', 'foxglove', 'frazzled',
    'frizzled', 'fuchsia', 'funny', 'gabby', 'galaxy', 'galvanize',
    'gazebo', 'giaour', 'gizmo', 'glowworm', 'glyph', 'gnarly', 'gnostic',
    'gossip', 'grogginess', 'haiku', 'haphazard', 'hyphen', 'iatrogenic',
    'icebox', 'injury', 'ivory', 'ivy', 'jackpot', 'jaundice', 'jawbreaker',
    'jaywalk', 'jazziest', 'jazzy', 'jelly', 'jigsaw', 'jinx', 'jiujitsu',
    'jockey', 'jogging', 'joking', 'jovial', 'joyful', 'juicy', 'jukebox',
    'jumbo', 'kayak', 'kazoo', 'keyhole', 'khaki', 'kilobyte', 'kiosk',
    'kitsch', 'kiwifruit', 'klutz', 'knapsack', 'larynx', 'lengths', 'lucky',
    'luxury', 'lymph', 'marquis', 'matrix', 'megahertz', 'microwave', 'mnemonic',
    'mystify', 'naphtha', 'nightclub', 'nowadays', 'numbskull', 'nymph',
    'onyx', 'ovary', 'oxidize', 'oxygen', 'pajama', 'peekaboo', 'phlegm', 'pixel', 'pizazz',
    'pneumonia', 'polka', 'pshaw', 'psyche', 'puppy', 'puzzling', 'quartz',
    'queue', 'quips', 'quixotic', 'quiz', 'quizzes', 'quorum', 'razzmatazz', 'rhubarb',
    'rhythm', 'rickshaw', 'schnapps', 'scratch', 'shiv', 'snazzy', 'sphinx',
    'spritz', 'squawk', 'staff', 'strength', 'strengths', 'stretch', 'stronghold',
    'stymied', 'subway', 'swivel', 'syndrome', 'thriftless', 'thumbscrew',
    'topaz', 'transcript', 'transgress', 'transplant', 'triphthong', 'twelfth',
    'twelfths', 'unknown', 'unworthy', 'unzip', 'uptown', 'vaporize',
    'vixen', 'vodka', 'voodoo', 'vortex', 'voyeurism', 'walkway', 'waltz',
    'wave', 'wavy', 'waxy', 'wellspring', 'wheezy', 'whiskey', 'whizzing',
    'whomever', 'wimpy', 'witchcraft', 'wizard', 'woozy', 'wristwatch', 'wyvern',
    'xylophone', 'yachtsman', 'yippee', 'yoked', 'youthful', 'yummy', 'zephyr',
    'zigzag', 'zigzagging', 'zilch', 'zipper', 'zodiac', 'zombie'
]

secret_word = possible_words[random.randint(0, len(possible_words))]
underlined_word = []
for i in range(0, len(secret_word)):
    underlined_word += '_'
chances_left = 5
print(secret_word)

while True:
    print(*underlined_word)
    guessed_letter = input('Guess a letter: ').lower()
    if guessed_letter.isalpha():
        if guessed_letter in secret_word:
            for x in range(0, len(secret_word)):
                if guessed_letter in secret_word[x]:
                    underlined_word[x] = guessed_letter
            if '_' not in underlined_word:
                print('You Win!!')
                break
            os.system('cls')
        else:
            chances_left -= 1
            os.system('cls')
            print('Wrong answer, Try again.')
            if chances_left == 0:
                print('Game over.')
                break
    else:
        print('Please type a letter, Try again.')


