from turtle import Turtle
import random

colors=['red','orange','yellow','green','blue','purple']
speed=10
starting_speed=5
class Car_manager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.all_cars=[]
        self.car_speed=starting_speed


    def create_car(self):
        random_choice=random.randint(1,6)
        if random_choice==6:

            new_car=Turtle("square")
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(colors))
            random_y=random.randint(-250,250)
            new_car.goto(300,random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.bk(self.car_speed)

    def level_up(self):
        self.car_speed+=speed
