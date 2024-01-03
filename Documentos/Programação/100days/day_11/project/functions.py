import random
from vars import cards_options

def start_game():
    answer = input('Do you wanna start the game?("y" or "n")\n').lower()
    if answer == 'y':
        return True
    else:
        return False

def treating_strs_player(x):

    while True:
        if 'King' in x:
            x.remove('King')
            x.append(10)
        elif 'Queen' in x:
            x.remove('Queen')
            x.append(10)
        elif 'Jack' in x:
            x.remove('Jack')
            x.append(10)
        else:
            break

        if 'Ace' in x:
            ace_option = int(input('You have an Ace, chose between 1 and 11:\n'))
            x.remove('Ace')
            if ace_option == (1 or 11):
                x.append(ace_option)
                continue
            else:
                ace_option = random.randint(1, 11)
                x.append(ace_option)
                continue
        else:
            break


    int_cards = []
    for i in range(0, len(x)):
        int_cards.append(int(x[i]))

    return int_cards

def treating_strs_computer(x):

    while True:
        if 'King' in x:
            x.remove('King')
            x.append(10)
        elif 'Queen' in x:
            x.remove('Queen')
            x.append(10)
        elif 'Jack' in x:
            x.remove('Jack')
            x.append(10)
        else:
            break


    if 'Ace' in x:
        while 'Ace' in x:
            x.remove('Ace')


    int_cards = []
    for i in range(0, len(x)):
        int_cards.append(int(x[i]))
        
    ace_option = 0
    if sum(int_cards) == 0:
        ace_option = 21
        int_cards.append(ace_option)
    elif sum(int_cards) in range(16, 20):
        ace_option = random.randint(1, 11)
        int_cards.append(ace_option)

    return int_cards

