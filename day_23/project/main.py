# turtle crossing

from turtle import Turtle, Screen
from cars import Cars
from animal import Animal
from scoreboard import ScoreBoard
from random import randrange
from time import sleep




screen = Screen()
screen.listen()
screen.title('Turtle Crossing')
screen.setup(800, 800)
screen.tracer(0)


turtle = Animal()
car = Cars()
hud = ScoreBoard()
car.hideturtle()



game_is_on = True

while game_is_on:
    sleep(.05)
    screen.onkeypress(turtle.move, 'w')
    screen.update()
    car.create_car()
    car.move()
    if turtle.ycor() >= 380:
        car.increase_velocity()
        hud.add_level()
        turtle.goto(0,-380)

    for c4r in car.cars:
        if c4r.distance(turtle) < 20:
            car.restart_speed()
            hud.restart_level()
            game_is_on = False
            restart_answer = screen.textinput('','Do you wanna restart the game? ')
            if restart_answer == 'y':
                turtle.goto(0, -380)
                game_is_on = True



screen.exitonclick()