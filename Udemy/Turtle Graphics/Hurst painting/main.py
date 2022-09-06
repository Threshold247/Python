from color import data
from turtle import Turtle, Screen, colormode
from random import choice

tim = Turtle()
screen = Screen()
colormode(255)
tim.shape('turtle')
tim.speed('fast')
tim.pu()
tim.goto(-300, -250)
number_of_dots = 100
tim.hideturtle()

for i in range(1, number_of_dots + 1):
    tim.fd(50)
    tim.dot(20, choice(data))

    if i % 10 == 0:
        tim.left(90)
        tim.fd(50)
        tim.left(90)
        tim.fd(500)
        tim.right(180)


screen.exitonclick()
