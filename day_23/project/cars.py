from turtle import Turtle, Screen
import random
from time import sleep

POSITIONS = (400, random.randrange(-340, 380, 40))
COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

class Cars(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.move_distance = 5
        self.bigger_num = 10
        for _ in range(10):
            self.create_car()


    def create_car(self):
        chance = random.randint(1, self.bigger_num)
        if chance == 1:
            POSITIONS = (400, random.randrange(-340, 380, 40))
            new_car = Turtle('square')
            new_car.shapesize(1, 2, 1)
            new_car.penup()
            new_car.seth(180)
            new_car.goto(POSITIONS)
            new_car.color(random.choice(COLORS))
            self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            if len(self.cars) >= 2:
                if car.distance(self.cars[-2]) > 30:
                    car.forward(self.move_distance)
            else:
                car.forward(self.move_distance)

    def increase_velocity(self):
        if self.bigger_num > 1:
            self.bigger_num -= 1
        if self.move_distance < 50:
            self.move_distance += 5

    def restart_speed(self):
        self.bigger_num = 10
        self.move_distance = 5