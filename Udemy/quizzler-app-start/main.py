from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface


question_bank = []
for question in question_data:
    # returns a dictionary
    # access the question value
    question_text = question["question"]
    # access the correct answer value
    question_answer = question["correct_answer"]
    # create tuple containing values for question text and question answer.
    new_question = Question(question_text, question_answer)
    # append the tuple to the question bank
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

# while quiz.still_has_questions():
#     quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
