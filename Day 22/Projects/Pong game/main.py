from turtle import Screen
from paddle import Paddle
import time

POSITION_LEFT = (-350, 0)
POSITION_RIGHT = (350, 0)

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("It's Pong Time")

paddle_left = Paddle(POSITION_LEFT)
paddle_right = Paddle(POSITION_RIGHT)

screen.tracer(0)
screen.listen()
screen.onkey(key="Up", fun=paddle_right.move_up)
screen.onkey(key="Down", fun=paddle_right.move_down)
screen.onkey(key="w", fun=paddle_left.move_up)
screen.onkey(key="s", fun=paddle_left.move_down)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)


screen.exitonclick()
