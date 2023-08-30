from turtle import Turtle,Screen
from snake import Snake
from food import Food
from score_board import Score_board
import time



screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("Black")
screen.title("My snake game")
screen.tracer(0)

score=Score_board()
food=Food()
snake=Snake()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


is_game_on=True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


    #detect food collision

    if snake.head.distance(food) < 15:
        food.random_food()
        snake.extend()
        score.score_increase()


    #detect wall collision
    if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor() > 275 or snake.head.ycor() < -275:
        # is_game_on=False
        score.reset()
        snake.reset()

    # detect collision with tail
    for segment in snake.segments[1:len(snake.segments)]:
        # if segment==snake.head:
        #     pass
        if snake.head.distance(segment) < 10:
            # is_game_on=False
            score.reset()
            snake.reset()







screen.exitonclick()