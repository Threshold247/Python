from turtle import Turtle

SCOREBOARD_ALIGNMENT = "center"
SCOREBOARD_FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
    # initialise high score to read the high_score.txt file and convert the text to integer
        with open("high_score.txt") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.pu()
        self.goto(0, 270)
        self.hideturtle()
        # inserts a method that updates the scoreboard
        self.update_score()

    def update_score(self):
        # setting up the scoreboard
        self.clear()
        self.write(f"Score:{self.score} High Score:{self.high_score}", align=SCOREBOARD_ALIGNMENT, font=SCOREBOARD_FONT)

    def increase_score(self):
        self.score = self.score + 1
        self.clear()
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            # replace the score in the high score txt file
            with open("high_score.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_score()



