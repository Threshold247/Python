from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.pu()
        self.move_x = 10
        self.move_y = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
        self.goto(new_x, new_y)

    def bounce(self):
        self.move_y *= -1

    def deflect(self):
        self.move_x *= -1
        # every time ball is deflected by a paddle increase ball speed
        self.move_speed *= 0.9

    def reset_ball(self):
        # reset ball position to center
        self.goto(0, 0)
        # reset ball speed to 0.1
        self.move_speed = 0.1
        self.deflect()
