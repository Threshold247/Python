import turtle
import pandas as pd

data = pd.read_csv("50_states.csv")

second_turtle = turtle.Turtle()
screen = turtle.Screen()
screen.title("Guess the State")
# change shape to custom shape
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

states = data["state"].tolist()
guessed_states = []

while len(guessed_states) < 50:

    user_answer = screen.textinput(title=f"Guess the State {len(guessed_states)}/50",
                                   prompt="Can you guess another State").title()
    # title capitalize the input.
    if user_answer == "Exit":
        # create a list to store missing states
        missing_state = []
        # go through all states in list
        for name in states:
            # check if name is not in guessed_states list add it to missing_name list
            if name not in guessed_states:
                missing_state.append(name)
        # create a dataframe
        new_Dataframe = pd.DataFrame(missing_state)
        # write dataframe to csv type
        new_Dataframe.to_csv("states-to-learn.csv")
        break

    if user_answer in states:
        guessed_states.append(user_answer)
        second_turtle.pu()
        second_turtle.hideturtle()
        # go through data frame and check which state name matches with the user answer
        state_data = data[data.state == user_answer]
        # grab the x co-ordinate from the state
        state_x_cord = int(state_data.x)
        # grab the y co-ordinate from the state
        state_y_cord = int(state_data.y)
        # move the turtle the state co-ordinates
        second_turtle.goto(state_x_cord, state_y_cord)
        # write the name of the state. note you can't use the state name data. it incl extra info
        second_turtle.write(user_answer, align="center")

    if len(guessed_states) == 50:
        print("You win!")

# keeps the screen active
# turtle.mainloop()
# states to learn
