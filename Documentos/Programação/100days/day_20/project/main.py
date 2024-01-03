from turtle import Turtle, Screen
from time import sleep

screen = Screen()
screen.listen()
screen.title('Snake Game')
screen.setup(600, 600)
screen.bgcolor('black')
screen.tracer(0)

starting_positions = [(0,0), (-20,0), (-40,0)]

segments = []

for position in starting_positions:
    
    new_segment = Turtle('square')
    new_segment.penup()
    new_segment.color('white')
    new_segment.goto(position)
    segments.append(new_segment)
    

game_is_on = True

screen.mainloop()