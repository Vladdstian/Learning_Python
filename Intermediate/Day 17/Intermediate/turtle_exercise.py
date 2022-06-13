# make the turtle go in a random direction and change color every time

from turtle import Turtle, Screen, colormode
from random import random, randint, choice

colormode(255)

# function done by me
# def change_direction(turtle_obj):
#     angle = [90, 180, 270, 360]
#     rand_angle_dir = randint(0, 3)
#     turn_direct = ["l", "r"]
#     rand_turn_dir = randint(0, 1)
#     if turn_direct[rand_turn_dir] == "l":
#         turtle_obj.left(angle[rand_angle_dir])
#     else:
#         turtle_obj.right(angle[rand_angle_dir])


def change_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color_tuple = (r, g, b)  # Tuples are immutable = cannot be changed
    return color_tuple


bob = Turtle()
# turtle appearance
bob.width(15)
bob.shape("circle")
bob.shapesize(0.1)
bob.speed("fastest")

# screen definition
screen = Screen()
while_exit = True

directions = [0, 90, 180, 270]
for _ in range(200):
    bob.pencolor(change_color())
    # function found in turtle documentation
    bob.setheading(choice(directions))
    bob.forward(25)

screen.exitonclick()
