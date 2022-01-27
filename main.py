from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time


L_PADDLE = (-350, 0)
R_PADDLE = (350, 0)

# Creating Screen
screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.tracer(0)

# Intitializing objects
player1 = Paddle(L_PADDLE)
player2 = Paddle(R_PADDLE)
ball = Ball()
score = Score()

# get user input
screen.listen()
screen.onkeypress(player1.move_up, 'z')
screen.onkeypress(player1.move_down, 's')
screen.onkeypress(player2.move_up, 'Up')
screen.onkeypress(player2.move_down, 'Down')

state_of_game = True

while state_of_game:
    screen.update()
    speed = ball.movespeed
    time.sleep(speed)
    ball.move()

    # Detect wall collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(player2) < 50 and ball.xcor() > 320 or ball.distance(player1) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        
    if ball.xcor() > 380:
        ball.reset_pos()
        score.right_increment()
   
    if ball.xcor() < -380:
        ball.reset_pos()
        score.left_increment()
        
screen.exitonclick()
