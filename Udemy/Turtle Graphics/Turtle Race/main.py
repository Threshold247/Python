import random
from turtle import Turtle, Screen
from random import randint, choice

screen = Screen()
screen.setup(width=500, height=400)
bet = screen.textinput(title="Bet on a turtle", prompt="Enter a colour").lower()
colors = ["red", "orange", "violet", "blue", "yellow", "brown"]
all_turtles = []
is_race_on = False

y_cord = -100
for turtle_index in range(0, 6):
    y_cord = y_cord + 30
    new_turtle = Turtle(shape="turtle")
    new_turtle.pu()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_cord)
    all_turtles.append(new_turtle)


if bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == bet:
                print(f"You won! The winning color is {winning_color}.")
            else:
                print(f"You lost. The winning color is {winning_color}.")
        random_distance = randint(0, 10)
        turtle.fd(random_distance)

screen.exitonclick()
