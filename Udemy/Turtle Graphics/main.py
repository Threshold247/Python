#####Turtle Intro######

import turtle as t
from turtle import Screen

tim = t.Turtle()
screen = Screen()

# Challenge 1 - Draw a Square

# tim.shape("turtle")
# tim.color("red")
#
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

# Challenge 2 - Draw a Dashed line
for _ in range(10):
    tim.fd(5)
    tim.pu()
    tim.fd(10)
    tim.pd()



screen.exitonclick()
