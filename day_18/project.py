# 1000000 paint

from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.pensize(10)
timmy.speed(8)
timmy.width(5)

screen = Screen()
screen.colormode(255)

def movement():

    colors = {
        'r': 0,
        'g': 0,
        'b': 0
    }

    turn_state = True

    for _ in range(20):

        timmy.pendown()

        for _ in range(20):

            for key in colors.keys():
                color = random.randint(0, 255)
                colors[key] = color

            timmy.color(colors['r'], colors['g'], colors['b'])

            timmy.dot(10)
            timmy.penup()
            timmy.forward(20)
        
        if turn_state == True:
            timmy.left(90)
            timmy.dot(10)
            timmy.forward(20)
            timmy.left(90)
            turn_state = False
        else:
            timmy.right(90)
            timmy.dot(10)
            timmy.forward(20)
            timmy.right(90)
            turn_state = True



movement()

screen.mainloop()