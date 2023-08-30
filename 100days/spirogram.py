import turtle
import random

t=turtle.Turtle()
turtle.colormode(255)
t.speed("fastest")
t.pensize(0.9)

def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    color=(r, g, b)
    return color



def draw_spriograph(size_of_angle):
    for _ in range(int(360/size_of_angle)):
        t.color(random_color())
        t.circle(100)
        current_head=t.heading()
        t.setheading(current_head+size_of_angle)


draw_spriograph(3)

screen=turtle.Screen()
screen.exitonclick()