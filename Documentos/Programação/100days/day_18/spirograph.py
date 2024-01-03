from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.speed(0)

screen = Screen()
screen.colormode(255)


def movement(size_gap):

    colors = {
        'r': 0,
        'g': 0,
        'b': 0
    }

    for _ in range(int(360 / size_gap)):

        for key in colors.keys():
            color = random.randint(0, 255)
            colors[key] = color

        timmy.color(colors['r'], colors['g'], colors['b'])

        timmy.circle(200)
        timmy.right(size_gap)


movement(5)

screen.mainloop()