from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('MS Sans Serif', 100, 'normal')

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        self.segments = []
        self.p1 = 0
        self.p2 = 0
        self.write(f'{self.p1}   {self.p2}', align=ALIGNMENT, font=FONT)


    def add_num(self, player):
        self.clear()
        if player == 'p1':
            self.p1 += 1
        else:
            self.p2 += 1

        self.write(f'{self.p1}   {self.p2}', align=ALIGNMENT, font=FONT)
        

    def final_score(self):
        final_score = Turtle()
        final_score.color('white')
        final_score.hideturtle()
        final_score.penup()
        final_score.goto(0, -40)
        final_score.write(f'Final score: {self.p1}', align=ALIGNMENT, font=FONT)


    def game_over(self, text):
        self.clear()
        self.goto(0, 0)
        self.write(f'GAME OVER! {text}', align=ALIGNMENT, font=FONT)
        self.final_score()
        self.p1 = 0


    def line_on_center(self):
        position = 60
        new_segment = Turtle('square')
        new_segment.color('white')
        new_segment.shapesize(2, .5, 1)
        new_segment.speed(0)
        new_segment.penup()
        new_segment.sety(-380)
        self.segments.append(new_segment)

        def create_segment():
            new_segment = Turtle('square')
            new_segment.color('white')
            new_segment.shapesize(2, .5, 1)
            new_segment.speed(0)
            new_segment.penup()
            new_segment.sety(self.segments[0].ycor() + position)
            self.segments.append(new_segment)

        for _ in range(13):
            create_segment()
            position += 60


