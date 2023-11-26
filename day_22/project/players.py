from turtle import Turtle


class Players(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('square')
        self.penup()
        self.shapesize(5, 1, 1)

    def move_up(self):
        if self.ycor() < 340:
            self.sety(self.ycor() + 30)
        
    def move_down(self):
        if self.ycor() > -340:
            self.sety(self.ycor() - 30)
