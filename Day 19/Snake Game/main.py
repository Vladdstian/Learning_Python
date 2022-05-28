from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")


def create_snake():
    snake = []
    position = []
    for _ in range(3):
        bob = Turtle(shape="square")
        bob.color("white")
        if len(position) == 0:
            position.append(bob.xcor())
            position.append(bob.ycor())
            position[0] = position[0] + 20
        else:
            bob.setposition(x=position[0], y=position[1])
            position[0] = position[0] + 20
        snake.append(bob)
    return snake


snake = create_snake()
screen.listen()
game_status = True


def move(snake_parts):


screen.exitonclick()
