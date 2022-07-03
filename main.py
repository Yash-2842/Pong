from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
r_paddle = Paddle(350)
l_paddle = Paddle(-350)
ball = Ball()
scoreboard = ScoreBoard()
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

is_gameon = True
speed = 0.1
while is_gameon:
    screen.update()
    ball.move()
    time.sleep(speed)
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        speed *= 0.9
    if ball.xcor() > 380:
        speed = 0.1
        ball.restart()
        scoreboard.lscore()
        time.sleep(2)
    if ball.xcor() < -380:
        speed = 0.1
        ball.restart()
        scoreboard.rscore()
        time.sleep(2)

screen.exitonclick()
