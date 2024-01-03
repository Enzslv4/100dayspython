# turtle challenge

from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape('turtle')

screen = Screen()
screen.colormode(255)

def movement():

    n = 3
    colors = {
        'r': 0,
        'g': 0,
        'b': 0
    }

    while n <= 10:

        for key in colors.keys():
            color = random.randint(0, 255)
            colors[key] = color

        timmy.pencolor(colors['r'], colors['g'], colors['b'])
        angle = 360 / n

        for _ in range(n):
            timmy.forward(100)
            timmy.right(angle)
        n += 1

movement()

screen.mainloop()