# turtle race betting
from turtle import Turtle, Screen
import random as r

screen = Screen()
screen_width = 400
screen_height = 300
total_turtles = 6
is_race_on = False

screen.setup(width=screen_width, height=screen_height)
# always use keyword arguments for a better readability of the code
turtle_colors = ["blue", "green", "red", "purple", "orange", "pink"]
turtle_pos = [-100, -60, -20, 20, 60, 100]

turtles = []
for index in range(total_turtles):
    bob = Turtle(shape="turtle")
    bob.penup()
    bob.color(turtle_colors[index])
    # print(bob.color()) test
    bob.setposition(x=-(screen_width / 2 - 20), y=turtle_pos[index])
    turtles.append(bob)

guess = screen.textinput(title="Make your bet!", prompt="What turtle do you think it will win? ")

if guess:
    is_race_on = True

while is_race_on:
    for _ in turtles:
        _.forward(r.randint(0, 10))
        if _.xcor() > screen_width/2 - 40:
            if guess == _.color()[0]:
                screen.textinput(title="Winner!",
                                 prompt=f"You won! The {_.color()[0]} turtle passed 1st the finish line!")
            else:
                screen.textinput(title="Looser!",
                                 prompt=f"You lost! The {_.color()[0]} turtle passed 1st the finish line!")
            is_race_on = False


screen.exitonclick()
