from turtle import Turtle
from time import sleep

ALIGNMENT = 'center'
FONT = ('MS Sans Serif', 30, 'normal')
FONT_GAME_OVER = ('MS Sans Serif', 50, 'normal')

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.sety(300)
        self.level = 0
        self.write(f'Level: {self.level}', align=ALIGNMENT, font=FONT)

    def add_level(self):
        self.clear()
        self.level += 1
        self.write(f'Level: {self.level}', align=ALIGNMENT, font=FONT)

    def restart_level(self):
        self.clear()
        self.level = 0
        self.write('GAME OVER!', align=ALIGNMENT, font=FONT_GAME_OVER)
        self.sety(200)
        self.clear()
        self.sety(300)
        self.write(f'Level: {self.level}', align=ALIGNMENT, font=FONT)
