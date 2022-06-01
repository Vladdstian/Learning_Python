from turtle import Turtle

POSITION = (0, 230)


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score_left = 0
        self.score_right = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(POSITION)
        self.update_score()

    def update_score(self):
        self.write(f"{self.score_left}    {self.score_right}", False, "center", font=("Arial", 50, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, "center", font=("Arial", 25, "normal"))

    def increase_score_left(self):
        self.score_left += 1
        self.clear()
        self.update_score()

    def increase_score_right(self):
        self.score_right += 1
        self.clear()
        self.update_score()
