import re

import pandas as pd

data = pd.read_csv("50_states.csv")

# capitalize the first letter of each word
test = input("Enter State:").lower()
# check if in input is in the Series. returns True or False
check = data["state"].str.findall(test, flags=re.IGNORECASE)

for item in check:
    if len(item) > 0:
        # Search through DataFrame if there is a state that matches the input
        answer = (data[data["state"] == item[0]])
        print(answer)
        test_answer = answer.values
        answer_list = test_answer[0]
        answer_x_cord = int(answer_list[1])
        answer_y_cord = int(answer_list[2])





