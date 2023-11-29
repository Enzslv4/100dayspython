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
        self.score = 0
        with open('day_20/project/data.txt') as file:
            num = file.read()
            self.high_score = int(num)
        self.write(f'Score: {self.score} Highest score: {self.high_score}', align=ALIGNMENT, font=FONT)

    def add_num(self):
        self.clear()
        self.score += 1
        self.write(f'Score: {self.score} Highest score: {self.high_score}', align=ALIGNMENT, font=FONT)


    def final_score(self):
        final_score = Turtle()
        final_score.color('white')
        final_score.hideturtle()
        final_score.penup()
        final_score.goto(0, -40)
        final_score.write(f'Final score: {self.score}', align=ALIGNMENT, font=FONT)


    def reset(self, text):
        self.clear()
        self.goto(0, 0)
        if self.score > self.high_score:
            with open('day_20/project/data.txt', 'w') as num:
                num.write(str(self.score))
        self.write(f'GAME OVER! {text}', align=ALIGNMENT, font=FONT)
        self.final_score()
        self.score = 0