from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
QUESTION_FONT = ('Ariel', 20, 'italic')


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20)
        self.window.configure(bg=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250, bg='white')
        self.score = Label(self.window, text=f"Score: 0", fg='white', bg=THEME_COLOR)
        self.question_text = self.canvas.create_text(
            150,
            125,
            text=f"Faz",
            font=QUESTION_FONT,
            fill="Black",
            width=280
        )
        self.checkmark_file = PhotoImage(file="../trivia_question_api/images/true.png")
        self.crossmark_file = PhotoImage(file="../trivia_question_api/images/false.png")
        self.checkmark_icon = Button(self.window, image=self.checkmark_file, command=self.true_pressed,
                                     highlightthickness=0)
        self.crossmark_icon = Button(self.window, image=self.crossmark_file, command=self.false_pressed,
                                     highlightthickness=0)
        self.score.grid(column=1, row=0)
        self.checkmark_icon.grid(column=0, row=2)
        self.crossmark_icon.grid(column=1, row=2)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # self.checkmark_icon.grid(row=2, column=0)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.window.after(1000, self.canvas.config(bg='green'))

        else:
            self.window.after(1000, self.canvas.config(bg='red'))
        self.window.after(1000, self.get_next_question)


