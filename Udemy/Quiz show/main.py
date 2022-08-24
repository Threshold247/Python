from question_model import Question
from data import question_data

# create list
question_bank = []
# loop through data
for items in question_data:
    # returns a dictionary
    # access the text value
    text = items['text']
    # access the answer value
    answer = items['answer']
    # create a new question model with a text and answer
    new_q = Question(text=text, answer=answer)
    # append new model to the empty list
    question_bank.append(new_q)


