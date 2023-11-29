from turtle import Screen
from time import sleep
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.listen()
screen.title('Snake Game')
screen.setup(600, 600)
screen.bgcolor('black')
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()


game_is_on = True


while game_is_on:
    screen.update()
    sleep(.1)

    snake.move()

    screen.onkeypress(snake.left, 'a')
    screen.onkeypress(snake.right, 'd')
    screen.onkeypress(snake.up, 'w')
    screen.onkeypress(snake.down, 's')
    screen.onkeypress(snake.increase_size, 'c')

    if snake.head.distance(food) < 15:
        snake.increase_size()
        food.goto_new_pos()
        score.add_num()


    if snake.is_on_borders() == True:
        score.reset(f'You hit a wall!')
        score.score = 0
        break

    if snake.hits_it_self():
        score.reset(f'You hit your own tail!')
        score.score = 0
        break
        


screen.exitonclick()