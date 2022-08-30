from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# create list
question_bank = []
# loop through data
for items in question_data:
    # returns a dictionary
    # access the text value
    text = items['question']
    # access the answer value
    answer = items['correct_answer']
    # create a new question model with a text and answer
    new_q = Question(text=text, answer=answer)
    # append new model to the empty list
    question_bank.append(new_q)

# create new object called quiz
quiz = QuizBrain(question_bank)

# loop will run while True
while quiz.still_has_questions():
    # generates a new question
    quiz.next_question()
print("Game completed")
print(f"Your final score is: {quiz.score}/{quiz.question_no}")
