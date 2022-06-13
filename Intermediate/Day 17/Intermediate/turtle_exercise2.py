# turtle spirograph drawing
from turtle import Turtle, Screen, colormode
from random import random, randint, choice
colormode(255)


def change_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color_tuple = (r, g, b)  # Tuples are immutable = cannot be changed
    return color_tuple


bob = Turtle()
# turtle properties
bob.speed("fastest")
bob.width(3)

angle = 5
total = 0
while total < 360:
    bob.pencolor(change_color())
    bob.circle(100)
    total += angle
    bob.left(angle)

screen = Screen()
screen.exitonclick()

# below code can be used to do the same as the while above and change the starting angle with an increment
current_heading = bob.heading()
bob.setheading(current_heading + 10)
