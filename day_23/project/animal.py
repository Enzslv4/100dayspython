from turtle import Turtle

STARTING_POSITION = (0, -380)
MOVE_DISTANCE = 10

class Animal(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.seth(90)
        self.penup()
        self.goto(STARTING_POSITION)

    def move(self):
        if self.ycor() < 400:
            self.forward(MOVE_DISTANCE)