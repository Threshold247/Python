from turtle import Screen
from scoreboard import Scoreboard
from paddle import Paddle


screen = Screen()

scoreboard = Scoreboard()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer()
paddle_1 = Paddle()

screen.listen()
screen.onkey(paddle_1.move_up, key="w")
screen.onkey(paddle_1.move_down, key="s")


screen.exitonclick()

