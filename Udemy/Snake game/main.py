from turtle import Turtle, Screen
import time

screen = Screen()

# setup screen
screen.setup(width=600, height=600)
# set background screen colour
screen.bgcolor("black")
# add a screen title
screen.title("My snake game")
screen.tracer(0)

# setting up starting x-coordinate for each segment
x_cord = 0
segments = []
# loop through 0 to 2
for snake_index in range(0, 3):
    # setting up snake segment and changing shape to square
    snake_segment = Turtle(shape="square")
    # pen up so that no trail is left when segments move into position
    snake_segment.pu()
    # change segment colour to white
    snake_segment.color("white")
    # each segment with have a different x-coordinate
    x_cord = x_cord - 20
    # sending segment to different position based on loop
    snake_segment.goto(x=x_cord, y=0)
    # add each segment object to segment list
    segments.append(snake_segment)

game_is_on = True
# use while loop
while game_is_on:
    # update screen
    screen.update()
    # add delay
    time.sleep(0.5)
    # looping through range. start point, end point, step parameter
    for seg_num in range(len(segments)-1, 0, -1):
        # setup new x_cord for each segment
        new_xcord = segments[seg_num-1].xcor()
        # setup new y_cord for each segment
        new_ycord = segments[seg_num-1].ycor()
        # each segment will move to the new coordinate
        segments[seg_num].goto(x=new_xcord, y=new_ycord)
    # first segment moves while following segment move to new coordinates
    segments[0].fd(20)


    def right():
        segments[0].setheading(0)


    def up():
        segments[0].setheading(90)


    def left():
        segments[0].setheading(180)


    def down():
        segments[0].setheading(270)


    screen.listen()
    screen.onkey(fun=right, key="d")
    screen.onkey(fun=up, key="w")
    screen.onkey(fun=left, key="a")
    screen.onkey(fun=down, key="s")


screen.exitonclick()

