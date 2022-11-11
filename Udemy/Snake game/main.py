from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

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
scoreboard = Scoreboard()
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
        # place another piece of food
        food.refresh()
        # add a segment onto the snake
        snake.extend_snake()
        # increase score
        scoreboard.increase_score()
    # detect collision with boundary wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset_snake()

    # detect collision with tail, used slicing method to exclude first segment aka snake.head
    for segment in snake.segments[1:]:
        # checks if head collides with all other segments
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset_snake()
screen.exitonclick()
