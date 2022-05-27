# event listeners in Turtle module
# higher order functions - commonly used in Python

from turtle import Turtle, Screen

bob = Turtle()
screen = Screen()


def move_forward():
    bob.forward(10)


screen.listen()
screen.onkey(key="space", fun=move_forward)
# the upper function takes another function as an input
# higher order function - function that can work with other functions
# the main function makes the input function do things with the other inputs/ variables
# for higher order functions use keyword arguments instead of positional arguments to avoid confusion
screen.exitonclick()

# more objects can be crated using the same blueprint
tommy = Turtle()
vlad = Turtle()
# each object can have different attributes and can do different things -
# this is known in programming as their state of an object

