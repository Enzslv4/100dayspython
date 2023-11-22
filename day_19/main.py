# etch a sketch

from turtle import Turtle, Screen
from functions import *
import time

screen = Screen()
screen.listen()
screen.title('Turtle Race')
screen.setup(1000, 800)
bet = screen.textinput('Turtle Race', 'Choose which turtle will win the race: ')

positions = {
    'blue': [leonardo, '', 'blue'],
    'orange': [michelangelo, '', 'orange'],
    'purple': [donatello, '', 'purple'],
    'red': [raphael, '', 'red'],
    'gray': [splinter, '', 'gray']
}


while True:

    condition = True
    
    game_logic()


    for _ in positions.keys():
        positions[_][1] = (positions[_][0]).pos()


    for i in positions.keys():
        if int(positions[i][1][0]) >= 450:
            condition = False
            winner = positions[i]
            if positions[i] == bet:
                screen.title(f'You Win!! {bet} is the winner!')
            else:
                screen.title(f'You Lose!! {positions[i][2]} is the winner!')
            
            restart_game = screen.textinput('Race Finished!!','Do you wanna restart the game? "y"es or "n"o: ')
            if restart_game == 'y':
                time.sleep(2)
            else:
                screen.bye()

    for k in positions.keys():
        set_speed(positions[k][0], condition)


    if condition == False:
        break


screen.mainloop()