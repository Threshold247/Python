class QuizBrain:

    def __init__(self, list):
        self.question_no = 0
        self.question_list = list

    def still_has_questions(self):
        if self.question_no < len(self.question_list):
            return True
        else:
            return False

    def next_question(self):
        current_question = self.question_list[self.question_no]
        # accessing the list position
        print(current_question)
        # adding 1 to the question number which starts at zero
        self.question_no += 1
        # ask user to input True or False. Displays question number and question text by accessing dictionary.text
        input(f"Q.{self.question_no}: {current_question.text} True/False: ")

