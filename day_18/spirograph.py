from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.speed(0)

screen = Screen()
screen.colormode(255)

def circle():
    for i in range(72):
        timmy.forward(20)
        timmy.right(5)

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

        timmy.color(colors['r'], colors['g'], colors['b'])

        circle()
        timmy.right(10)


movement()

screen.mainloop()