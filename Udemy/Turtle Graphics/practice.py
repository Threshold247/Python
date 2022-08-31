from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
screen = Screen()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("blue")


def square_fill():
    timmy_the_turtle.color("blue", "green")
    timmy_the_turtle.begin_fill()
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(90)
    timmy_the_turtle.stamp()
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(90)
    timmy_the_turtle.stamp()
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(90)
    timmy_the_turtle.forward(100)
    timmy_the_turtle.end_fill()


def square():
    timmy_the_turtle.color("blue")
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(90)
    timmy_the_turtle.stamp()
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(90)
    timmy_the_turtle.stamp()
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(90)
    timmy_the_turtle.forward(100)


square()
square_fill()
timmy_the_turtle.forward(0)
square()
square_fill()
screen.exitonclick()













