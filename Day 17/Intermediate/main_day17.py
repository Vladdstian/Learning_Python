# Turtle graphics
# !always search for documentation on each library

# import turtle
# bob = turtle.Turtle()  -> long version

from turtle import Turtle, Screen
# from turtle import *  -> this statement imports everything in that module as if it were in that module !!!BAD PRACTICE
# import turtle as t  -> imports the module with a custom name (in this case 't')
# bob = t.Turtle()
import random


def dash_line(length, turtle_object):
    my_turtle = turtle_object
    line_length = length
    space = 0
    while line_length > 0:
        if space % 2 == 0:
            my_turtle.pendown()
            my_turtle.forward(10)
        else:
            my_turtle.penup()
            my_turtle.forward(10)
        line_length -= 10
        space += 1
    my_turtle.pendown()


def draw_square(side_l, turtle_object):
    side = side_l
    turtle = turtle_object
    for i in range(0, 4):
        turtle.forward(side)
        turtle.right(90)


def draw_shape(side_len, sides, turtle_object):
    side = side_len
    num_side = sides
    angle = 360 / sides
    my_turtle = turtle_object
    for _ in range(num_side):
        my_turtle.forward(side)
        my_turtle.right(angle)


def random_color(turtle_object):
    random_r = random.random()
    random_g = random.random()
    random_b = random.random()
    turtle_object.pencolor(random_r, random_g, random_b)


bob = Turtle()  # -> short version
bob.shape("turtle")

side_length = 100
for _ in range(4, 20):
    draw_shape(side_length, _, bob)
    random_color(bob)

bob.color("purple")

# draw a dashed lane
dash_line(200, bob)
draw_square(100, bob)

# screen properties
screen = Screen()
screen.exitonclick()


# pypi.org for custom packages -> Pycharm can install any of those packages
import heroes  # custom package that has not been already installed
print(heroes.gen())
