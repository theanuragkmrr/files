from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.hideturtle()
        self.color("black")
        self.penup()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-280, 250)
        self.write(f"Level : {self.score}", font=("Arial", 20, "italic"))


    def score_up(self):
        self.score+=1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write(f"game over", align="center", font=("Arial", 20, "normal"))

    def logo(self):
        self.goto(290,270)
        self.write(f"@theanuragkmr", align="right", font=("Arial", 15, "normal"))


