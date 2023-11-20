# turtle random path challenge

from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.pensize(10)
timmy.speed(8)

screen = Screen()
screen.colormode(255)

def movement():

    colors = {
        'r': 0,
        'g': 0,
        'b': 0
    }

    directions = [0, 90, 180, 270]

    while True:

        for key in colors.keys():
            color = random.randint(0, 255)
            colors[key] = color

        timmy.color(colors['r'], colors['g'], colors['b'])
        timmy.forward(50)
        timmy.setheading(random.choice(directions))

movement()

screen.mainloop()