from turtle import Turtle
import random

DIRECTION = random.randrange(60, 150)

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.seth(DIRECTION)


    def set_new_heading(self):
        DIRECTION = random.randrange(60, 150)
        self.seth(DIRECTION)
    
    def hits_wall(self):
        if (self.ycor() >= 380) or (self.ycor() < -380):
            self.seth(self.heading() - 2 * self.heading())
        

    def hits_player(self, player):
        if self.distance(player) < 15:
            self.seth(self.heading() - 2 * self.heading())

    def gets_out_the_field(self):
        if (self.xcor() >= 600):
            return True
        if (self.xcor() <= -600):
            return True