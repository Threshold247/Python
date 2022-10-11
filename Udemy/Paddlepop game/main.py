from turtle import Screen
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball
import time

screen = Screen()

scoreboard = Scoreboard()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Paddle pop game")
screen.tracer(0)
paddle_1 = Paddle((-350, 0), color= "white")
paddle_2 = Paddle((350, 0), color="blue")
ball = Ball()


screen.listen()
screen.onkey(paddle_1.move_up, key="w")
screen.onkey(paddle_1.move_down, key="s")
screen.onkey(paddle_2.move_up, key="o")
screen.onkey(paddle_2.move_down, key="l")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    # detect collision with paddle1 and paddle 2
    if ball.distance(paddle_1) < 50 and ball.xcor() < -320 or ball.distance(paddle_2) < 50 and ball.xcor() > 320:
        ball.deflect()

    if ball.xcor() > 400:
        print("paddle 1 scored")
        ball.reset_ball()
        scoreboard.increase_score1()

    if ball.xcor() < -400:
        print("paddle 2 scored")
        ball.reset_ball()
        scoreboard.increase_score2()

screen.exitonclick()

