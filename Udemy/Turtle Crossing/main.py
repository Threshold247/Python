import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Frogger")
screen.tracer(0)
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_up, key="w")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    scoreboard.update_level()
    screen.update()
    car_manager.create_car()
    car_manager.car_move()
    # detect collision with car
    for car in car_manager.all_cars:
        # loop through the list of cars and check if turtle is in close to car object
        if car.distance(player) < 25:
            # stop the game
            game_is_on = False
            scoreboard.game_over()
    # detect if player gets across
    if player.is_at_finish():
        player.go_to_start()
        car_manager.increase_speed()
        scoreboard.increase_level()

screen.exitonclick()
