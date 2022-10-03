from turtle import Screen
from scoreboard import Scoreboard
from paddle1 import Paddle1
from paddle2 import Paddle2

screen = Screen()

scoreboard = Scoreboard()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Paddle pop game")
screen.tracer()
paddle_1 = Paddle1()
paddle_2 = Paddle2()

screen.listen()
screen.onkey(paddle_1.move_up, key="w")
screen.onkey(paddle_1.move_down, key="s")
screen.onkey(paddle_2.move_up2, key="o")
screen.onkey(paddle_2.move_down2, key="l")

screen.exitonclick()
