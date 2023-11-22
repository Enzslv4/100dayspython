# 1000000 paint

from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.pensize(10)
timmy.speed(8)
timmy.width(5)
timmy.penup()

screen = Screen()
screen.colormode(255)

def movement():
    
    timmy.hideturtle()
    timmy.setheading(210)
    timmy.forward(300)
    timmy.setheading(0)
    

    colors = {
        'r': 0,
        'g': 0,
        'b': 0
    }

    turn_state = True


    for _ in range(10):

        for _ in range(10):

            for key in colors.keys():
                color = random.randint(0, 255)
                colors[key] = color

            timmy.dot(20, (colors['r'], colors['g'], colors['b']))
            timmy.forward(50)
        
        if turn_state == True:
            timmy.left(90)
            timmy.dot(20)
            timmy.forward(50)
            timmy.left(90)
            turn_state = False
        else:
            timmy.right(90)
            timmy.dot(20)
            timmy.forward(50)
            timmy.right(90)
            turn_state = True


movement()

screen.mainloop()