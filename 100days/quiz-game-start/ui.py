from tkinter import *
from quiz_brain import QuizBarin
THEME_COLOR="#375362"

class QuizInterface:
    def __init__(self,quiz_brain:QuizBarin):
        self.quiz=quiz_brain
        self.window=Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
        self.score_label=Label(text="score: 0",fg="white",bg=THEME_COLOR)
        self.score_label.grid(row=0,column=1)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)
        self.question=self.canvas.create_text(150,125,
                                width=280,
                                text="Something gona be here",
                                fill=THEME_COLOR,
                                font=("Arial",20,"italic"))
        turu=PhotoImage(file="./images/true.png")
        self.turu_btn=Button(image=turu,highlightthickness=0,command=self.Tru)
        self.turu_btn.grid(row=2,column=0)
        false=PhotoImage(file="./images/false.png")
        self.false_btn = Button(image=false, highlightthickness=0,command=self.Fals)
        self.false_btn.grid(row=2, column=1)
        self.get_question()
        self.window.mainloop()


    def get_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_question():
            q_txt=self.quiz.next_question()
            self.score_label.config(text=f"Score : {self.quiz.score}")
            self.canvas.itemconfig(self.question,text=q_txt)
        else:
            self.canvas.itemconfig(self.question,text="You have reached end of the question")
            # self.turu_btn.config(state="disable")
            # self.false_btn.config(state="disable")

    def Tru(self):
        is_right=self.quiz.check_ans("True")
        self.give_feedback(is_right)

    def Fals(self):
        is_right=self.quiz.check_ans("False")
        self.give_feedback(is_right)

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000,self.get_question)
