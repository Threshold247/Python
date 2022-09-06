import turtle
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
tim.shape("turtle")

# press w to move forward
# press s to move backward


def move_forward():
    tim.fd(10)


def move_backward():
    tim.bk(10)


def turn_left():
    tim.lt(5)


def turn_right():
    tim.rt(5)


def clear():
    tim.pu()
    tim.home()
    tim.clear()
    tim.pd()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
