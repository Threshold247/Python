from turtle import Turtle

SCOREBOARD_ALIGNMENT = "center"
SCOREBOARD_FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score1 = 0
        self.score2 = 0
        self.color("white")
        self.pu()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Score", align=SCOREBOARD_ALIGNMENT, font=SCOREBOARD_FONT)
        self.write(f"Player 1 {self.score1}", align="left", font=SCOREBOARD_FONT)
        self.write(f"Player 2 {self.score2}", align="right", font=SCOREBOARD_FONT)
