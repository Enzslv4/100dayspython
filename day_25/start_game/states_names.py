from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('MS Sans Serif', 10, 'normal')

class StatesNames(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.hideturtle()
        self.penup()
        
    def set_pos(self, x, y, name):
        self.goto(x, y)
        self.write(name, align=ALIGNMENT, font=FONT)
