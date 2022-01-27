from turtle import Turtle
import random

default_speed = 0.07

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.y_move = 10
        self.x_move = 10
        self.movespeed = default_speed
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
    
    def bounce_y(self):
        self.y_move *= -1
        self.movespeed *= 0.9
        
    def bounce_x(self):
        self.x_move *= -1
        self.movespeed *= 0.9
    
    def reset_pos(self):
        self.goto(0, 0)
        self.movespeed = default_speed
        self.bounce_x()