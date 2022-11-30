import pandas as pd

data = pd.read_csv("50_states.csv")

state = data["state"]
x_cord = data["x"]
y_cord = data["y"]


test = input("Enter State:")
check = test in data["state"].values
if check:
    answer = (data[data["state"] == test])
    print(answer)
    answer_x_cord = answer["x"]
    answer_y_cord = answer["y"]





