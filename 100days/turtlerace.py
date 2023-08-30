from turtle import Turtle, Screen
import random

is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your Bet", prompt="Which turtle win thr race? Enter a color: ")

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_position = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle in range(0, 6):
    newturtle = Turtle(shape="turtle")
    newturtle.penup()
    newturtle.color(colors[turtle])
    newturtle.goto(x=-230, y=y_position[turtle])
    all_turtles.append(newturtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:

                print(f"you won! {winning_color}")
            else:
                print(f"you lose! the {winning_color} turtle won the race")
        dist = random.randint(0, 10)
        turtle.forward(dist)

print(all_turtles)
screen.exitonclick()
