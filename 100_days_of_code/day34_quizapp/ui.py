from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
timer = None

class Ui:
    def __init__(self, quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz App")
        self.window.config(background=THEME_COLOR, padx=20, pady=20)
        self.current_score = 0

        self.text_score = Label(text=f"Score: {self.current_score}", background=THEME_COLOR, pady=20, fg="white")
        self.text_score.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Text", font=("Ariel", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)
        

        self.img_true = PhotoImage(file="day34_quizapp/images/true.png")
        self.img_false = PhotoImage(file="day34_quizapp/images/false.png")

        self.btn_true = Button(image=self.img_true, command=self.check_true)
        self.btn_true.grid(row=2, column=0)
        self.btn_false = Button(image=self.img_false, command=self.check_false)
        self.btn_false.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()


    def end_of_quiz(self):
        self.canvas.itemconfig(self.question_text, text=f"You reached the End of Quiz and you scored {self.quiz.score}")
        self.btn_false.config(state="disabled")
        self.btn_true.config(state="disabled")

    def get_next_question(self):
        self.canvas.config(background="white")
        self.btn_false.config(state="normal")
        self.btn_true.config(state="normal")
        try:
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=question_text)
        except IndexError:
            self.end_of_quiz()
        
    def check_true(self):
        is_user_correct = self.quiz.check_answer(user_answer="True")
        self.process_answer(is_user_correct)

    def check_false(self):
        is_user_correct = self.quiz.check_answer(user_answer="False")
        self.process_answer(is_user_correct)

    def process_answer(self, is_user_correct):
        global timer
        self.btn_false.config(state="disabled")
        self.btn_true.config(state="disabled")
        if timer:
            self.window.after_cancel(timer)
        if is_user_correct:
            self.canvas.config(background="green")
            self.text_score.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.config(background="red")
        timer = self.window.after(1000, self.get_next_question)
