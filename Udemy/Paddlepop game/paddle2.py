from paddle1 import Paddle1


MOVEMENT = 30


class Paddle2(Paddle1):

    def __init__(self):
        super().__init__()
        self.goto(x=250, y=0)
        self.color("blue")

    def move_up2(self):
        y = self.ycor() + MOVEMENT
        # if the
        if y > 280:
            y = 280

        self.sety(y)

    def move_down2(self):
        y = self.ycor() - MOVEMENT
        # if the
        if y < -280:
            y = - 280

        self.sety(y)




