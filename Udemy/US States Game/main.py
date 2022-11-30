import turtle
from data import data


screen = turtle.Screen()
screen.title("Guess the State")
# change shape to custom shape
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

# game_on = True

# while game_on:


user_answer = screen.textinput(title="Guess the State", prompt="Can you guess another State")
print(user_answer)
if data["state"] == user_answer:
    print(True)

# keeps the screen active
turtle.mainloop()


