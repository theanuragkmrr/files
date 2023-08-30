import turtle
import random
t = turtle.Turtle()
turtle.colormode(255)

colors = ['Grey', 'Purple', 'Blue', 'Green', 'Orange', 'Red','yellow', 'IndianRed']
direct = [0,90,180,270]

def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    random_color=(r, g, b)
    return random_color

for _ in range(200):
    t.pensize(10)
    t.speed("fast")
    t.color(random_color())
    t.forward(20)
    t.setheading(random.choice(direct))







screen=turtle.Screen()
screen.exitonclick()