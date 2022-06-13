from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")


def create_snake():
    initial_snake = []
    for _ in range(3):
        segment = []
        bob = Turtle(shape="square")
        bob.color("white")
        segment_id = {"id": bob}
        seg_position = {"position": [0, 0]}
        segment.append(seg_position)
        segment.append(segment_id)
        initial_snake.append(segment)


    return initial_snake


snake = create_snake()
screen.listen()
game_status = True


screen.exitonclick()
