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

game_logic()
condition = True

while condition:

    for i in positions.keys():
        positions[i][1] = (positions[i][0]).pos()
        set_speed(positions[i][0], condition)
        if int(positions[i][1][0]) >= 450:
            condition = False
            winner = positions[i]
            if positions[i] == bet:
                screen.title(f'You Won!! {bet} is the winner!')
            else:
                screen.title(f'You Lost!! {positions[i][2]} is the winner!')
            
            restart_game = screen.textinput('Race Finished!!','Do you wanna restart the game? "y"es or "n"o: ')
            if restart_game == 'y':
                condition = True
                game_logic()
            else:
                screen.bye()


screen.mainloop()