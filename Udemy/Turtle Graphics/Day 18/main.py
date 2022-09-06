# Turtle Intro
import math
import turtle as t
from random import randint, choice
from turtle import Screen
from turtle import colormode

tim = t.Turtle()
screen = Screen()
tim.shape("turtle")


# Challenge 1 - Draw a Square


# tim.color("red")
#
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

# Challenge 2 - Draw a Dashed line
# for _ in range(10):
#     tim.fd(5)
#     tim.pu()
#     tim.fd(10)
#     tim.pd()


# Challenge 3 - Draw shapes and change colours
# def shapes(side):
#     angle = 360
#     tim.seth(180)
#     for _ in range(side):
#         tim.rt(angle / side)
#         tim.fd(100)
#
#
# mylist = ["green", "blue", "red", "yellow", "orange", "purple", "pink", "light blue"]
# for shape in range(3, 11):
#     tim.color(mylist[shape-3])
#     shapes(shape)

# Challenge 4 - Random Walk
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
#            "SeaGreen"]
# direction = [0, 90, 180, 270]
# # specify speed for turtle
# tim.speed("slow")
# # change turtle pen size
# tim.pensize(5)

# for _ in range(100):
#     tim.fd(30)
#     # accessed random.choice
#       tim.seth(choice(direction))
#     # tim.seth(random.randrange(0, 360, 90))
#     # accessed random.randint to generate colours (R, G, B)
#     tim.color(choice(colours))

# Challenge 5 Changing colours without using list
#
# direction = [0, 90, 180, 270]
# # specify speed for turtle
# tim.speed("slow")
#
#
# def random_color():
#     r = randint(0, 255)
#     g = randint(0, 255)
#     b = randint(0, 255)
#     my_tuple = (r, g, b)
#     return my_tuple
#
#
# # color module required to generate random colours
# t.colormode(255)
# # change turtle pen size
# tim.pensize(5)
# for _ in range(100):
#     tim.fd(30)
#     # accessed random.choice
#     tim.seth(choice(direction))
#     # tim.seth(random.randrange(0, 360, 90))
#     # accessed random.randint to generate colours (R, G, B) via a function
#     tim.color(random_color())
#     # alternative method tim.color(randint(0,255),randint(0,255),randint(0,255))

# Challenge 6 Make a colourful Spirograph
colormode(255)


# def random_color():
#     r = randint(0, 255)
#     g = randint(0, 255)
#     b = randint(0, 255)
#     my_tuple = (r, g, b)
#     return my_tuple
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
           "SeaGreen"]

tim.pensize(1)
tim.speed("fastest")


def draw_spirograph(tilt):
    angle = 360
    my_range = (math.ceil(angle/tilt)) + 1
    for _ in range(my_range):
        tim.color(choice(colours))
        tim.circle(100)
        tim.right(tilt)


draw_spirograph(8)
screen.exitonclick()
