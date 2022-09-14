from turtle import Turtle, Screen

screen = Screen()
MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        # setting up starting x-coordinate for each segment
        x_cord = 0
        # loop through 0 to 2
        for snake_index in range(0, 3):
            # setting up snake segment and changing shape to square
            snake_segment = Turtle(shape="square")
            # pen up so that no trail is left when segments move into position
            snake_segment.pu()
            # change segment colour to white
            snake_segment.color("white")
            # each segment with have a different x-coordinate
            x_cord -= 20
            # sending segment to different position based on loop
            snake_segment.goto(x=x_cord, y=0)
            # add each segment object to segment list
            self.segments.append(snake_segment)

    def move_snake(self):
        # looping through range. start point, end point, step parameter
        for seg_num in range(len(self.segments) - 1, 0, -1):
            # setup new x_cord for each segment
            new_xcord = self.segments[seg_num - 1].xcor()
            # setup new y_cord for each segment
            new_ycord = self.segments[seg_num - 1].ycor()
            # each segment will move to the new coordinate
            self.segments[seg_num].goto(x=new_xcord, y=new_ycord)
            # first segment moves while following segment move to new coordinates
        self.head.fd(MOVE_DISTANCE)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)


