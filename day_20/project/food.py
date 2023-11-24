from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(.5, .5)
        self.color('red')
        self.speed(0)
        xcor = random.randint(-280, 280)
        ycor = random.randint(-280, 280)
        self.goto(xcor, ycor)

    def goto_new_pos(self):
        xcor = random.randint(-280, 280)
        ycor = random.randint(-280, 280)
        self.goto(xcor, ycor)