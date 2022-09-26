from turtle import Turtle

SCOREBOARD_ALIGNMENT = "center"
SCOREBOARD_FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.pu()
        self.goto(0, 270)
        self.hideturtle()
        # inserts a method that updates the scoreboard
        self.update_score()

    def update_score(self):
        # setting up the scoreboard
        self.write(f"Score:{self.score}", align=SCOREBOARD_ALIGNMENT, font=SCOREBOARD_FONT)

    def increase_score(self):
        self.score = self.score + 1
        self.clear()
        self.update_score()

    def hit_wall(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=SCOREBOARD_ALIGNMENT, font=SCOREBOARD_FONT)
