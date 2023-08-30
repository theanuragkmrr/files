from turtle import Screen
from player import Player
from car_manager import Car_manager
from scoreboard import Scoreboard
import time

screen=Screen()
screen.setup(600,600)
screen.tracer(0)


player=Player()
car=Car_manager()
score=Scoreboard()


screen.listen()
screen.onkey(player.move,"Up")

game_is_on=True

while game_is_on:
  time.sleep(0.1)
  screen.update()
  car.create_car()
  car.move_cars()
  score.logo()

  for cars in car.all_cars:
    if cars.distance(player)< 20:
      game_is_on=False
      score.game_over()

  if player.ycor()>280:
    player.goto(0,-280)
    car.level_up()
    score.score_up()


screen.exitonclick()