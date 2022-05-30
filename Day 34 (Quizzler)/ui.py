from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 16, "italic")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.label = Label(
            bg=THEME_COLOR, text=f"Score: 0", fg="white")
        self.label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=275,
            text="Some Question Text",
            fill=THEME_COLOR,
            font=FONT
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20)

        self.true_image = PhotoImage(file="images/true.png")
        self.true = Button(image=self.true_image,
                           command=self.true_button)
        self.true.grid(column=0, row=2)

        self.false_image = PhotoImage(file="images/false.png")
        self.false = Button(image=self.false_image,
                            command=self.false_button)
        self.false.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            question = self.quiz.next_question()
            self.label.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question_text, text=question)
        else:
            self.canvas.itemconfig(
                self.question_text,
                text=f"You've reached {self.quiz.score}/{len(self.quiz.question_list)}"
            )
            self.true.config(state="disabled")
            self.false.config(state="disabled")

    def true_button(self):
        self.feedback(self.quiz.check_answer("true"))

    def false_button(self):
        self.feedback(self.quiz.check_answer("false"))

    def feedback(self, answer):
        if answer:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
