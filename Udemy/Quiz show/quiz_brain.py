class QuizBrain:

    def __init__(self, list):
        self.question_no = 0
        self.question_list = list
        self.score = 0

    def still_has_questions(self):
        if self.question_no < len(self.question_list):
            return True
        else:
            return False

    def next_question(self):
        current_question = self.question_list[self.question_no]
        # accessing the list position
        # print(current_question)
        # adding 1 to the question number which starts at zero
        self.question_no += 1
        # ask user to input True or False. Displays question number and question text by accessing dictionary.text
        user_choice = input(f"Q.{self.question_no}: {current_question.text} True/False: ")
        pc_answer = current_question.answer
        self.check_answer(user_choice, pc_answer)

    def check_answer(self, user_choice, pc_answer):
        if user_choice.lower() == pc_answer.lower():
            print("Correct")
            self.score += 1
        else:
            print("Incorrect")
        print(f"The correct answer is: {pc_answer}")
        print(f"Your current score is: {self.score}/{self.question_no}")
        print("\n")

