from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz App")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Create Scoreboard

        self.scoreboard_label = Label(text=f"Score:", font=("Arial", 10), fg="white", bg=THEME_COLOR, highlightthickness=0)
        self.scoreboard_label.grid(row=0, column=1)
        # Create  text box

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125
                                                     , width=280
                                                     , text=f"Stuff"
                                                     , fill=THEME_COLOR
                                                     , font=("Arial", 20, "italic")
                                                     )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Create buttons
        true_answer = PhotoImage(file="images/true.png")
        self.known_btn = Button(image=true_answer, highlightthickness=0, command=self.true_answer)
        self.known_btn.grid(row=2, column=0)

        false_answer = PhotoImage(file="images/false.png")
        self.unknown_btn = Button(image=false_answer, highlightthickness=0, command=self.false_answer)
        self.unknown_btn.grid(row=2, column=1)

        self.get_question()

        self.window.mainloop()

    def get_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions:
            self.scoreboard_label.config(text=f"Score:{self.quiz.score}/{self.quiz.question_number}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz")
            self.known_btn.config(state="disabled")
            self.unknown_btn.config(state="disabled")

    def true_answer(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_answer(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(2000, func=self.get_question)




