from turtle import Turtle, Screen
import random

POSITIONS = (400, random.randrange(-340, 380, 40))
COLORS = [
    random.randrange(0, 255),
    random.randrange(0, 255),
    random.randrange(0, 255)
]

class Cars(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color(COLORS)
        self.seth(90)
        self.penup()
        self.shapesize(3,1,1)
        self.goto(POSITIONS)
        self.cars = []
        self.x_move = 5

    def move(self):
        
        new_x = self.xcor() + self.x_move
        self.setx(new_x)

    def create_new_car(self):
        POSITIONS = (random.randrange(-380, 380, 20), random.randrange(-340, 380, 40))
        COLORS = [
            random.randrange(0, 255),
            random.randrange(0, 255),
            random.randrange(0, 255)
        ]
        new_car = Turtle()
        new_car.shape('square')
        new_car.color(COLORS)
        new_car.seth(90)
        new_car.penup()
        new_car.shapesize(3,1,1)
        new_car.goto(POSITIONS)
        self.cars.append(new_car)