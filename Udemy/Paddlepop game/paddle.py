from turtle import Turtle

MOVEMENT = 20


class Paddle(Turtle):

    def __init__(self, position, color):
        super().__init__()
        # position takes a tuple
        self.goto(position)
        # set shape
        self.shape("square")
        # set shape
        self.shapesize(stretch_wid=5, stretch_len=1)
        # set color (will use argument)
        self.color(color)
        self.pu()

    def move_up(self):
        new_y = self.ycor() + MOVEMENT
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - MOVEMENT
        self.goto(self.xcor(), new_y)




