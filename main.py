from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.01)
    # TODO 1 -- Move the ball in a continuous manner:
    ball.move()

    # TODO 2: Detect the collision of the ball with the wall:
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # TODO 3: Detect the collision of the ball with the paddles:
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # TODO 4: Detect when the right paddle misses the ball:
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # TODO 5: Detect when the left paddle misses the ball:
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
