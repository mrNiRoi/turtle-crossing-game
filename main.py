import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
score = Scoreboard()

screen.listen()
screen.onkeypress(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.drive()

    for c in car.all_cars:
        if player.distance(c) < 20:
            score.game_over()
            game_is_on = False

    if player.ycor() > 300:
        score.update()
        car.speedup()
        player.reset()

screen.exitonclick()