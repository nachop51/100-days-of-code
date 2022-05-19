import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move, "Up")

counter = 0
game_is_on = True
while game_is_on:
    counter += 1
    time.sleep(0.1)
    car_manager.move(counter)
    screen.update()
    if player.check_y():
        player.next_level()
        scoreboard.increment_level()
        car_manager.increase_speed()
    collide = car_manager.collision(player)
    if collide:
        game_is_on = False
        scoreboard.game_over()

screen.exitonclick()
