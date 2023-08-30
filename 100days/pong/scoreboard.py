from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score=0
        self.r_score=0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.update_scoreboard()



    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 250)
        self.write(f"{self.l_score}", font=("Arial", 20, "italic"))
        self.goto(100, 250)
        self.write(f" {self.r_score}", font=("Arial", 20, "italic"))

    def l_point(self):
        self.l_score+=1
        self.update_scoreboard()

    def r_point(self):
        self.r_score+=1
        self.update_scoreboard()





    def score_increase(self):
        self.l_score += 1
        self.r_score += 1
        self.clear()
        self.update_scoreboard()
