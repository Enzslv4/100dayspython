# Pong Game

from turtle import Screen
from players import Players
from scoreboard import ScoreBoard
from ball import Ball
from time import sleep

screen = Screen()
screen.listen()
screen.title('Snake Game')
screen.setup(1200, 800)
screen.bgcolor('black')
screen.tracer(0)

hud = ScoreBoard()
p1 = Players()
p1.speed(0)
p1.goto(-580,0)
p1.speed()
p2 = Players()
p2.speed(0)
p2.goto(580,0)
p2.speed()


hud.line_on_center()
ball = Ball()


screen.onkeypress(p1.move_up, 'w')
screen.onkeypress(p1.move_down, 's')
screen.onkeypress(p2.move_up, 'i')
screen.onkeypress(p2.move_down, 'k')

game_is_on = True


while game_is_on:
    screen.update()
    sleep(.03)
    ball.forward(15)
    ball.hits_wall()
    ball.hits_player(p1)
    ball.hits_player(p2)
    if ball.gets_out_the_field() == True:
        if ball.xcor() <= -600:
            hud.add_num('p1')
            restart = screen.textinput('Game Over!' ,'Do you wanna restart? ')
            if restart == 'y':
                ball.set_new_heading()
                ball.goto(0,0)
                continue
            else:
                break

    print(ball.heading())

screen.mainloop()