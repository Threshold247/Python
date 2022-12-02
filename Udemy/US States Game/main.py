import turtle
import pandas as pd
import re

data = pd.read_csv("50_states.csv")

second_turtle = turtle.Turtle()
screen = turtle.Screen()
screen.title("Guess the State")
# change shape to custom shape
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

game_on = True

while game_on:

    user_answer = screen.textinput(title="Guess the State", prompt="Can you guess another State")
    check = data["state"].str.findall(user_answer, flags=re.IGNORECASE)
    # if check returns True
    for name in check:
        if len(name) > 0:
            # Search through DataFrame if there is a state that matches the input
            answer = (data[data["state"] == name[0]])
            print(f'original answer: {answer}')
            # returns actual values in series
            answer = answer.values
            # navigate through list by indexing
            print(f'converted answer: {answer}')
            answer_list = answer[0]
            print(f'answer in list: {answer_list}')
            # convert value into integer
            state_name = answer_list[0]
            state_x_cord = float(answer_list[1])
            state_y_cord = float(answer_list[2])
            second_turtle.pu()
            second_turtle.hideturtle()
            second_turtle.goto(state_x_cord, state_y_cord)
            second_turtle.write(state_name, align="center")
# keeps the screen active
turtle.mainloop()


