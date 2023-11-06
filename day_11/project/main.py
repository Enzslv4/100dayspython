# blackjack game

import random
from functions import if_ace

player_cards = []
computer_cards = []

cards_dict = {
    'King': 10,
    'Queen': 10,
    'Jack': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2,
    'Ace': 1
}

while True:
    start_game = input('Do you wanna start the game?("y" or "n")\n')
    if start_game == 'n':
        break
    
    for i in range(0, 2):
        player_cards.append(random.choice(list(cards_dict.items())))
        computer_cards.append(random.choice(list(cards_dict.items())))
        i += 1

    print(if_ace(player_cards.keys()))

    sum_player_cards = 0
    for i in range(0, len(player_cards)):
        sum_player_cards += player_cards[i][1]

    print(sum_player_cards)

    print(f'Your cards are "{player_cards[0][0]}" and "{player_cards[1][0]}"',
            f'And one of the computers cards is "{player_cards[0][0]}"',
            sep='\n'
        )

    if sum_player_cards > 21:
        print('Game Over! You lose!')
        break
    elif 1 and 10 in player_cards:
        print('...')

    add_card = input('Do you want to add a new card?("y" or "n")\n')

    if add_card == 'y':
        player_cards.append(random.choice(list(cards_dict.items())))
        print('Your cards are:', *player_cards[0])
    else:
        ...
    

