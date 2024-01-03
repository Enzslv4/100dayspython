# trying to make a sinusoid on turtle

from turtle import Turtle, Screen
import random
import math

timmy = Turtle()

screen = Screen()
screen.colormode(255)

pi = math.pi

def movement():
    ang = 30 # the initial angle
    a = 100 # amplitude
    f = 50 # frequency
    t = 0 # time
    x = 0 # x value on grafic
    c = 300000000 # light speed
    wave_length = c / f
    omega = 2 * pi
    k = omega / wave_length
    
    while True:
        t += 1
        inside_sen = (k*x) - (omega * t) + ang # everything that goes inside the sen func
        if inside_sen > 360:
            divisor = math.floor(inside_sen / 360)
            inside_sen = inside_sen - 360 * divisor
        elif inside_sen < 0:
            inside_sen *= -1
            divisor = math.floor(inside_sen / 360)
            inside_sen = (-1) * (inside_sen - 360 * divisor)
        rad = math.radians(inside_sen)
        seno = math.sin(rad)
        y = a * seno
        timmy.setpos(x, y)
        x += 1

movement()

screen.mainloop()