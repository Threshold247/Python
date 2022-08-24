from main import question_bank
class QuizBrain:

    def __init__(self, list):
        self.question_no = 0
        self.question_list = list


test = QuizBrain(question_bank)
print(test)