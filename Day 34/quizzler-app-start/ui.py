from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface():

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.score_label = Label(text=f"Score {self.quiz.score}:{self.quiz.question_number}",
                                 fg="white", bg=THEME_COLOR,
                                 font=("arial", 20, "italic"))
        self.score_label.grid(row=0, column=0, columnspan=2)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, width=280,
                                                     text="Aqui va la pregunta",
                                                     fill=THEME_COLOR,
                                                     font=("arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2)

        self.x_image = PhotoImage(file="./images/false.png")
        self.button_x = Button(image=self.x_image, highlightthickness=0, borderwidth=0, command=self.is_false)
        self.button_x.grid(row=3, column=0, sticky=W, pady=20)

        self.y_image = PhotoImage(file="./images/true.png")
        self.button_y = Button(image=self.y_image, highlightthickness=0, borderwidth=0, command=self.is_true)
        self.button_y.grid(row=3, column=1, sticky=E, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():

            self.canvas.itemconfig(self.question_text, fill=THEME_COLOR)
            self.score_label.config(text=f"Score {self.quiz.score}:{self.quiz.question_number}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz!", fill="black")
            self.canvas.config(bg="white")
            self.button_x.config(state="disabled")
            self.button_y.config(state="disabled")

    def is_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def is_false(self):
        is_wrong = self.quiz.check_answer("False")
        self.give_feedback(is_wrong)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="lightgreen")
            self.canvas.itemconfig(self.question_text, fill="white")
        else:
            self.canvas.config(bg="red")
            self.canvas.itemconfig(self.question_text, fill="white")
        self.window.after(200, self.get_next_question)
