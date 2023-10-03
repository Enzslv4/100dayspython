# treasure island

import os

print('Welcome to the treasure island.', 'Your mission is to find the treasure.', sep='\n')
print()
text_1 = [
    "1. You've entered a forked street on the way to the seaport,", 
    "the left one is full of cars,",
    "but the right one seems to be free,",
]

text_2 = [
    "2. Once you have entered the seaport,",
    "you found that there is no time to get the nearest ship,",
    "so you need to decide rather you swim to the island,",
    "or you wait for the next ship."
]

text_3 = [
    "So, you succesfully went to the next ship and eventualy to the island,",
    "then you take of your treasure map from inside of your backpack,",
    "and begin to search the chest,",
    "but you had to enter a dark zone,",
    "once you're inside, you see raising 3 diferents lights from the background",
    "but, you can't go back and need to choose one of then"
]

i = 0

while i < len(text_1):
    print(text_1[i])
    i += 1

decision_1 = input("which one do u chose? ")

if decision_1 == 'l':
    os.system('cls')
    i = 0
    while i < len(text_2):
        print(text_2[i])
        i += 1
    decision_2 = input('Swim or Wait? ')
    if decision_2 == 'w':
        os.system('cls')
        i = 0
        while i < len(text_3):
            print(text_3[i])
            i += 1
        decision_3 = input("Which way('r'ed, 'b'lue or 'y'ellow)? ")
        if decision_3 == ('b' or 'r'):
            print('Game Over!')
        elif decision_3 == 'y':
            print('You win!')
    else:
        print('Game Over!')
else:
    print('Game Over!')