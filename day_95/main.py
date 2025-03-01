import turtle
import random
import time

# Setup the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Space Invaders")
screen.setup(width=600, height=600)
screen.tracer(0)

# Player (Spaceship)
player = turtle.Turtle()
player.shape("triangle")
player.color("white")
player.penup()
player.goto(0, -250)
player.setheading(90)

# Player movement
def move_left():
    x = player.xcor() - 20
    if x > -280:
        player.setx(x)

def move_right():
    x = player.xcor() + 20
    if x < 280:
        player.setx(x)

screen.listen()
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")

# Aliens
aliens = []
for i in range(5):
    alien = turtle.Turtle()
    alien.shape("square")
    alien.color("red")
    alien.penup()
    alien.goto(random.randint(-200, 200), 200)
    aliens.append(alien)

# Bullets
bullet = turtle.Turtle()
bullet.shape("circle")
bullet.color("yellow")
bullet.penup()
bullet.hideturtle()
bullet_speed = 20

def fire_bullet():
    if not bullet.isvisible():
        bullet.goto(player.xcor(), player.ycor())
        bullet.showturtle()

def move_bullet():
    if bullet.isvisible():
        bullet.sety(bullet.ycor() + bullet_speed)
        if bullet.ycor() > 280:
            bullet.hideturtle()

screen.onkey(fire_bullet, "space")

# Game Loop
running = True
while running:
    screen.update()
    move_bullet()
    
    for alien in aliens:
        alien.sety(alien.ycor() - 1)
        if alien.distance(player) < 20:
            print("Game Over!")
            running = False
        if bullet.distance(alien) < 20:
            alien.goto(random.randint(-200, 200), 200)
            bullet.hideturtle()
    
    time.sleep(0.05)

turtle.done()
