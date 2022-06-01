from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time

POSITION_LEFT = (-350, 0)
POSITION_RIGHT = (350, 0)

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("It's Pong Time")

paddle_left = Paddle(POSITION_LEFT)
paddle_right = Paddle(POSITION_RIGHT)
ball = Ball()
score = Score()

screen.tracer(0)
screen.listen()
screen.onkey(key="Up", fun=paddle_right.move_up)
screen.onkey(key="Down", fun=paddle_right.move_down)
screen.onkey(key="w", fun=paddle_left.move_up)
screen.onkey(key="s", fun=paddle_left.move_down)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -300:
        ball.bounce_y()

    # Detect collision with left and right paddles
    if ball.distance(paddle_right) < 50 and ball.xcor() > 320 or ball.distance(paddle_left) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect collision with walls and increase score for players
    if ball.xcor() > 380 or ball.xcor() < -380:
        if ball.x_move < 0:
            score.increase_score_right()
        else:
            score.increase_score_left()
        ball.bounce_x()
        ball.restart_ball()


screen.exitonclick()
