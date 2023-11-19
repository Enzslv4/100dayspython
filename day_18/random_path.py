# turtle challenge

from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.pensize(10)

screen = Screen()
screen.colormode(255)

def movement():

    colors = {
        'r': 0,
        'g': 0,
        'b': 0
    }

    while True:

        for key in colors.keys():
            color = random.randint(0, 255)
            colors[key] = color

        timmy.pencolor(colors['r'], colors['g'], colors['b'])

        side = random.choice(['l', 'r'])

        if side == 'l':
            timmy.forward(50)
            timmy.left(90)
        else:
            timmy.forward(50)
            timmy.right(90)

movement()

screen.mainloop()