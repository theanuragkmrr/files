import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("PING PONG Game")
screen.tracer(0)


r_p=Paddle((380,0))
l_p=Paddle((-380,0))
ball=Ball()
score=Scoreboard()

# ball.setx(ball.xcor() + ball.dx)
# ball.sety(ball.ycor() + ball.dy)

screen.listen()
screen.onkey(r_p.up,"Up")
screen.onkey(r_p.down,"Down")

screen.onkey(l_p.up,"w")
screen.onkey(l_p.down,"s")



game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()

    # detect collision with ball

    if ball.ycor() >280 or ball.ycor()<-280:
        ball.bounce_y()

    #detect collision with r_p
    if ball.distance(r_p)<50 and ball.xcor()>350 or ball.distance(l_p)<40 and ball.xcor()>-360:
        ball.bounce_x()

    #detect miss right side
    if ball.xcor()>400 :
        ball.reset()
        score.l_point()

    # detect miss left side

    if ball.xcor()<-400 :
        ball.reset()
        score.r_point()




screen.exitonclick()