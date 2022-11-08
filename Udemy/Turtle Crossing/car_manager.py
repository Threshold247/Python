from turtle import Turtle
from random import choice, randint
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []

    def create_car(self):
        # create random number between 1 and 6
        random_choice = randint(1, 6)
        # if the random number is 1 then create a car
        if random_choice == 1:
            # create car from Turtle class
            new_car = Turtle()
            # new does not leave behind trail
            new_car.pu()
            # new car colour generated from array radomnly
            new_car.color(choice(COLORS))
            # new car shape size
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            # new car shape
            new_car.shape("square")
            # generate random Y co-ordinate for each car
            random_y = randint(-250, 250)
            # new car will always start at teh same X co-ordinate but the Y co-ordinate will be random
            new_car.goto(300, random_y)
            # add the new car to the list called all_cars
            self.all_cars.append(new_car)

    def car_move(self):
        # loop through the list
        for car in self.all_cars:
            # each car will move at specific pace initially
            car.bk(STARTING_MOVE_DISTANCE)
