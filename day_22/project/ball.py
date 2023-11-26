from turtle import Turtle
import random

x_dir = random.randint(30, 90)
y_dir = random.randint(30, 90)

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.x_move = 10
        self.y_move = 10


    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    
    def hits_wall(self):
        if self.ycor() >= 380 or self.ycor() < -380:
            self.y_move *= -1

    def hits_player(self):
            self.x_move *= -1

    def gets_out_the_field(self):
        if self.xcor() > 600 or self.xcor() < -600:
            self.x_move *= -1
            return True
