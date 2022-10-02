from turtle import Turtle, Screen

screen = Screen()
MOVEMENT = 30


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.goto(x=-250, y=0)
        self.shape("square")
        self.shapesize(4, 1)
        self.color("white")
        self.pu()

    def move_up(self):
        y = self.ycor() + MOVEMENT
        # if the
        if y > 280:
            y = 280

        self.sety(y)

    def move_down(self):
        y = self.ycor() - MOVEMENT
        # if the
        if y < -280:
            y = - 280

        self.sety(y)


