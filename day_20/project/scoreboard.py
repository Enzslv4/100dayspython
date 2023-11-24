from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 20, 'normal')

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        self.num = 0
        self.write(f'Score: {self.num}', align=ALIGNMENT, font=FONT)

    def add_num(self):
        self.clear()
        self.num += 1
        self.write(f'Score: {self.num}', align=ALIGNMENT, font=FONT)


    def final_score(self):

        final_score = Turtle()
        final_score.color('white')
        final_score.hideturtle()
        final_score.penup()
        final_score.goto(0, -40)
        final_score.write(f'Final score: {self.num}', align=ALIGNMENT, font=FONT)


    def game_over(self, text):
        self.clear()
        self.goto(0, 0)
        self.write(f'GAME OVER! {text}', align=ALIGNMENT, font=FONT)
        self.final_score()
        self.num = 0