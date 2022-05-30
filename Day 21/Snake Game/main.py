from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

starting_positions = [(0, 0), (-20, 0), (-40, 0)]

snake = []
position = 0
for segment in range(3):
    bob = Turtle(shape="square")
    bob.color("white")
    bob.penup()
    bob.setposition(starting_positions[position])
    snake.append(bob)
    position += 1



screen.exitonclick()
