from turtle import Turtle

class Animal(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.seth(90)
        self.penup()
        self.goto(0,-380)