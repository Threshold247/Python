from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
screen = Screen()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("blue")


def square_fill():
    timmy_the_turtle.color("blue", "green")
    timmy_the_turtle.begin_fill()
    for _ in range(4):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(90)
        timmy_the_turtle.stamp()
    timmy_the_turtle.end_fill()


def square():
    timmy_the_turtle.color("blue")
    for _ in range(4):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(90)
        timmy_the_turtle.stamp()


square()
timmy_the_turtle.setheading(90)
square_fill()
timmy_the_turtle.setheading(180)
square()
timmy_the_turtle.setheading(270)
square_fill()
screen.exitonclick()

