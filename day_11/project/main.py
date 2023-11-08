# blackjack game

from os import system as clear_console
import art
import random
import functions
import vars

print(art.logo)
print('Welcome to the BlackJack game!!')

while True:

    answer = functions.start_game()
    if answer == True:
        clear_console('cls')
    else:
        break

    vars.player_cards = []
    vars.computer_cards = []

    for i in range(2):
        vars.player_cards.append(random.choice(list(vars.cards_options)))
        vars.computer_cards.append(random.choice(list(vars.cards_options)))

    print(f'Your cards are "{vars.player_cards[0]}" and "{vars.player_cards[1]}"',
            f"And one of the computer's cards is '{vars.computer_cards[random.randint(0,1)]}'",
            sep='\n'
        )
    
    vars.player_cards = functions.treating_strs_player(vars.player_cards)
    vars.computer_cards = functions.treating_strs_computer(vars.computer_cards)
    
    vars.sum_player_cards = sum(vars.player_cards)
    vars.sum_computer_cards = sum(vars.computer_cards)

    while (vars.sum_player_cards or vars.sum_computer_cards) < 21:

        add_card = input('\nDo you want to add a new card?("y" or "n")\n')

        if add_card == 'y':
            vars.player_cards.append(random.choice(list(vars.cards_options)))
            vars.player_cards = functions.treating_strs_player(vars.player_cards)
            vars.sum_player_cards = sum(vars.player_cards)
            print(f"Your cards are: {vars.player_cards}, With a total of: {vars.sum_player_cards}")
        elif add_card == 'n':
            break
    
    if vars.sum_player_cards > 21:
        print('Game Over! You have over 21!')
        break
    elif vars.sum_computer_cards > 21:
        print('You won! The computer has more than 21!')
        break
    elif vars.sum_player_cards > vars.sum_computer_cards:
        print(f'You won! You had {vars.sum_player_cards}, and the computer had {vars.sum_computer_cards}')
        break
    elif vars.sum_player_cards < vars.sum_computer_cards:
        print(f'You lose! You had {vars.sum_player_cards}, and the computer had {vars.sum_computer_cards}')
        break
    else:
        print(f'You draw! You had {vars.sum_player_cards}, and the computer had {vars.sum_computer_cards}')
        break
    
    
