import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=1,stretch_wid=1)
        self.color("red")
        self.speed("fast")
        self.random_food()

    def random_food(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-275, 275)
        self.goto(random_x, random_y)