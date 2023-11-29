from turtle import Turtle, Screen
import random

STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
TURN_RADIUS = {
    'up': 90, 
    'down': -90, 
    'left': 180, 
    'right': 0
}

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle('square')
            new_segment.penup()
            new_segment.color('white')
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.segments[0].forward(MOVE_DISTANCE)
        
    def left(self):
        if self.head.heading() != TURN_RADIUS['right']:
            for seg_num in range(len(self.segments) - 1, 0, -1):
                new_x = self.segments[seg_num - 1].xcor()
                new_y = self.segments[seg_num - 1].ycor()
                self.segments[seg_num].goto(new_x, new_y)
                self.segments[0].seth(TURN_RADIUS['left'])

    def right(self):
        if self.head.heading() != TURN_RADIUS['left']:
            for seg_num in range(len(self.segments) - 1, 0, -1):
                new_x = self.segments[seg_num - 1].xcor()
                new_y = self.segments[seg_num - 1].ycor()
                self.segments[seg_num].goto(new_x, new_y)
                self.segments[0].seth(TURN_RADIUS['right'])

    def up(self): 
         if self.head.heading() != TURN_RADIUS['down']:
            for seg_num in range(len(self.segments) - 1, 0, -1):
                new_x = self.segments[seg_num - 1].xcor()
                new_y = self.segments[seg_num - 1].ycor()
                self.segments[seg_num].goto(new_x, new_y)
                self.segments[0].seth(TURN_RADIUS['up'])

    def down(self):
         if self.head.heading() != TURN_RADIUS['up']:
            for seg_num in range(len(self.segments) - 1, 0, -1):
                new_x = self.segments[seg_num - 1].xcor()
                new_y = self.segments[seg_num - 1].ycor()
                self.segments[seg_num].goto(new_x, new_y)
                self.segments[0].seth(TURN_RADIUS['down'])

    def increase_size(self):
        new_segment = Turtle('square')
        new_segment.penup()
        new_segment.color('white')
        last_pos_segment = (self.segments[len(self.segments) - 1]).pos()
        self.segments.append(new_segment)
        new_segment.goto(last_pos_segment)

    def is_on_borders(self):

        if int(self.segments[0].xcor()) >= 300:
            return True
        if int(self.segments[0].ycor()) >= 300:
            return True
        if int(self.segments[0].xcor()) <= -300:
            return True
        if int(self.segments[0].ycor()) <= -300:
            return True
        
    def hits_it_self(self):
        for segment in self.segments[1:]:
            if self.head.distance(segment) < 10:
                return True
