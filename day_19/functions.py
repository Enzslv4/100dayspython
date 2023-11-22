from turtle import Turtle, Screen
import random

race_finish = Turtle()
race_start = Turtle()
leonardo = Turtle()
michelangelo = Turtle()
donatello = Turtle()
raphael = Turtle()

splinter = Turtle()
splinter.color('gray')
splinter.shape('arrow')
splinter.penup()

turtles = {
    'race_finish': {
        'name': race_finish,
        'speed': 0,
        'init_pos': (450, 350),
        'direction': -90,
        'final_pos': (450, -350),
        },
    'race_start': {
        'name': race_start,
        'speed': 0,
        'init_pos': (-400, 350),
        'direction': -90,
        'final_pos': (-400, -350),
        },
    'leonardo': {
        'name': leonardo,
        'init_pos': (-400, 300),
        'color': 'blue'
        },
    'michelangelo': {
        'name': michelangelo,
        'init_pos': (-400, 150),
        'color': 'orange'
        },
    'donatello': {
        'name': donatello,
        'init_pos': (-400, 0),
        'color': 'purple'
        },
    'raphael': {
        'name': raphael,
        'init_pos': (-400, -150),
        'color': 'red'
        },
}


def game_logic():

    splinter.setpos(-400, -300)
    

    def turtle_racers(turtles):
        '''Easy way to make the racers'''
        
        turtles['name'].color(turtles['color'])
        turtles['name'].penup()
        turtles['name'].shape('turtle')
        turtles['name'].setpos(*(turtles['init_pos']))

    def race_lines(turtles):
        '''Easy way to draw the lines'''

        turtles['name'].penup()
        turtles['name'].speed(turtles['speed'])
        turtles['name'].setpos(*(turtles['init_pos']))
        turtles['name'].setheading(turtles['direction'])
        turtles['name'].pendown()
        turtles['name'].setpos(*(turtles['final_pos']))
        turtles['name'].hideturtle()


    race_lines(turtles['race_start'])
    race_lines(turtles['race_finish'])

    turtle_racers(turtles['leonardo'])
    turtle_racers(turtles['michelangelo'])
    turtle_racers(turtles['donatello'])
    turtle_racers(turtles['raphael'])


def set_speed(turtle, x):
    if x == True:
        turtle.forward(random.randint(10, 70))
