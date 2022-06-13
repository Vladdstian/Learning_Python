from turtle import Turtle

MOVE_POSITION = 20


class Paddle(Turtle):
    def __init__(self, position_tuple):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.setposition(position_tuple)
        self.shapesize(stretch_wid=5, stretch_len=1)

    def move_up(self):
        if self.ycor() < 240:
            new_y = self.ycor() + MOVE_POSITION
            self.goto(x=self.xcor(), y=new_y)

    def move_down(self):
        if self.ycor() > -240:
            new_y = self.ycor() - MOVE_POSITION
            self.goto(x=self.xcor(), y=new_y)
