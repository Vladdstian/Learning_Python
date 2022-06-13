# use W, A, S, D keys to draw using Bob the Turtle
from turtle import Turtle, Screen

bob = Turtle()
screen = Screen()


def move_forward():
    bob.forward(10)


def move_backwards():
    bob.backward(10)


def move_clockwise():
    bob.right(10)


def move_counter_clockwise():
    new_heading = bob.heading() + 10
    bob.setheading(new_heading)


def clear():
    bob.clear()
    bob.penup()
    bob.home()
    bob.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_counter_clockwise)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
