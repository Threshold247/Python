from turtle import Turtle
from random import randint


class Food(Turtle):

    def __init__(self):
        # initialise super class which is Turtle
        super().__init__()
        # make shape
        self.shape("circle")
        # pen up
        self.pu()
        # reduce size to 10 by 10
        self.shapesize(0.5, 0.5)
        # change colour
        self.color("white")
        # increase speed
        self.speed("fastest")
        # set position randomly
        self.refresh()

    def refresh(self):
        self.goto(x=(randint(-280, 280)), y=(randint(-280, 280)))

