from turtle import Turtle

POSITION = (0, 270)


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(POSITION)
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", False, "center", font=("Arial", 20, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()
