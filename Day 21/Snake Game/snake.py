from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.setposition(position)
            self.segments.append(new_segment)

    def up(self):
        if self.head.heading() == 270 or self.head.heading() == 90:
            pass
        else:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() == 90 or self.head.heading() == 180:
            pass
        else:
            self.head.setheading(270)

    def left(self):
        self.head.left(90)

    def right(self):
        self.head.right(90)

    def move(self):
        for seg_number in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_number - 1].xcor()
            new_y = self.segments[seg_number - 1].ycor()
            self.segments[seg_number].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
