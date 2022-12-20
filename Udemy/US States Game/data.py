import re

import pandas as pd

data = pd.read_csv("50_states.csv")


# capitalize the first letter of each word
test = input("Enter State:").title()
# check if in input is in the Series. returns True or False
states_data = data["state"].tolist()
check = test in states_data
if check:
    answer = data[data.state == test]
    print(answer)
    print(answer.x)







