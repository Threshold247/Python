from turtle import Turtle

SCOREBOARD_ALIGNMENT = "center"
SCOREBOARD_FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.pu()
        self.hideturtle()
        self.left_side = 0
        self.right_side = 0
        self.update_score()

    def update_score(self):
        self.goto(-100, 200)
        self.write(self.left_side, align="center", font=SCOREBOARD_FONT)
        self.goto(100, 200)
        self.write(self.right_side, align="center", font=SCOREBOARD_FONT)

    def increase_score1(self):
        self.left_side += 1
        self.clear()
        self.update_score()

    def increase_score2(self):
        self.right_side += 1
        self.clear()
        self.update_score()

