# blackjack game

import random
import functions
import vars

while True:
    start_game = input('Do you wanna start the game?("y" or "n")\n')
    if start_game == 'n':
        break
    
    for i in range(0, 2):
        vars.player_cards.append(random.choice(list(vars.cards_options)))
        vars.computer_cards.append(random.choice(list(vars.cards_options)))
        i += 1

    print(f'Your cards are "{vars.player_cards[0]}" and "{vars.player_cards[1]}"',
            f'And one of the computers cards is "{vars.computer_cards[random.randint(0,1)]}"',
            sep='\n'
        )
    
    vars.player_cards = functions.treating_strs(vars.player_cards)
    vars.computer_cards = functions.treating_strs(vars.computer_cards)
    
    for i in range(0, len(vars.player_cards)):
        vars.sum_player_cards += vars.player_cards[i]

    if vars.sum_player_cards > 21:
        print('Game Over! You have over 21!')
        break

    
    for i in range(0, len(vars.computer_cards)):
        vars.sum_computer_cards += vars.computer_cards[i]

    if vars.sum_computer_cards > 21:
        print('You won! The computer has more than 21!')
        break

    add_card = input('Do you want to add a new card?("y" or "n")\n')

    if add_card == 'y':
        vars.player_cards.append(random.choice(list(vars.cards_dict.items())))
        print('Your cards are:', *vars.player_cards[0])
    elif add_card == 'n':
        if vars.sum_player_cards > vars.sum_computer_cards:
            print(f'You won! You had {vars.sum_player_cards}, and the computer had {vars.sum_computer_cards}')
        else:
            print(f'You lose! You had {vars.sum_player_cards}, and the computer had {vars.sum_computer_cards}')
    

