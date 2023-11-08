def treating_strs(x):

    if 'King' in x:
        x.remove('King')
        x.append(10)
    elif 'Queen' in x:
        x.remove('Queen')
        x.append(10)
    elif 'Jack' in x:
        x.remove('Jack')
        x.append(10)

    if 'Ace' in x:
        ace_option = int(input('Yoy have an Ace, chose between 1 and 11:\n'))
        x.remove('Ace')
        x.append(ace_option)

    int_cards = []
    for i in range(0, len(x)):
        int_cards[i] += int(x[i])

    return int_cards
