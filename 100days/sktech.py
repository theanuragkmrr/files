from turtle import Turtle,Screen
t=Turtle()
screen=Screen()

def forward():
    t.forward(10)

def back():
    t.bk(10)

def left():
    t.lt(10)

def right():
    t.rt(10)
def clear():
    t.clear()
    t.penup()
    t.home()


screen.listen()
screen.onkey(key="w", fun=forward)
screen.onkey(key="s", fun=back)
screen.onkey(key="a", fun=left)
screen.onkey(key="d", fun=right)
screen.onkey(key="c", fun=clear)
screen.exitonclick()