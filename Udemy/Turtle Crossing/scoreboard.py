from turtle import Turtle

FONT = ("Courier", 20, "normal")
SCOREBOARD_ALIGNMENT = "left"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.pu()
        self.color("blue")
        self.goto(-270, 260)
        self.hideturtle()
        self.update_level()

    def update_level(self):
        # setting up the scoreboard
        self.write(f"Level:{self.level}", align=SCOREBOARD_ALIGNMENT, font=FONT)

    def increase_level(self):
        self.level += 1
        self.clear()
        self.update_level()

    def game_over(self):
        self.color("red")
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)






