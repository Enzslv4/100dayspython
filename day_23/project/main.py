# turtle crossing

from turtle import Turtle, Screen
from cars import Cars
from animal import Animal
from random import randrange
from time import sleep




screen = Screen()
screen.listen()
screen.colormode(255)
screen.title('Turtle Crossing')
screen.setup(800, 800)
screen.tracer(0)

car = Cars()
turtle = Animal()
colors = [
    randrange(0, 255),
    randrange(0, 255),
    randrange(0, 255)
]

# car.color(colors[0], colors[1], colors[2])

game_is_on = True

for _ in range(20):
    car.create_new_car()

screen.tracer(1)

while game_is_on:
    sleep(.1)
    if car.xcor() >= -380 or car.xcor() <= 380:
        car.move()



screen.mainloop()