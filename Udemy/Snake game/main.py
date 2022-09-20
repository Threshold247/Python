from turtle import Screen
from random import randint
import time
from snake import Snake
from food import Food

screen = Screen()

# setup screen
screen.setup(width=600, height=600)
# set background screen colour
screen.bgcolor("black")
# add a screen title
screen.title("My snake game")
screen.tracer(0)
#   create snake class
snake = Snake()
#   create food class
food = Food()
#  initialise event listener
screen.listen()
screen.onkey(snake.right, key="Right")
screen.onkey(snake.up, key="Up")
screen.onkey(snake.left, key="Left")
screen.onkey(snake.down, key="Down")

game_is_on = True
# use while loop
while game_is_on:
    # update screen
    screen.update()
    # add delay
    time.sleep(0.2)
    snake.move_snake()
    # detect collision wih food by using distance method from Turtle class
    if snake.head.distance(food) < 15:
        print("Yummy")
        food.refresh()

screen.exitonclick()

