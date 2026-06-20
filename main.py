import time
import turtle
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
screen.onkey(player.move_up, "Up")

sixth_counter = 0
car_manager.add_new_car()
game_is_on = True
while game_is_on:
    sixth_counter += 1
    time.sleep(0.1)
    screen.update()
    if sixth_counter == 5:
        sixth_counter = 0
        car_manager.add_new_car()

    car_manager.move_cars()

    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_is_on = False
            print("Collision")
            scoreboard.game_over()

    if player.is_at_finish_line():
        scoreboard.increase_level()
        player.reset_position()
        car_manager.increase_speed()



screen.exitonclick()