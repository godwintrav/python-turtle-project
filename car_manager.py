from turtle import Turtle
from typing import Tuple
import random

from car import Car

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
POSITIONS = list(range(-250, 251, 20))

class CarManager:

    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def add_new_car(self):
        car_color = random.choice(COLORS)
        y_pos = random.randint(-250, 250)
        self.generate_car(car_color, pos=(300, y_pos))

    def generate_car(self, color, pos: Tuple[float, float]):
        car = Car(color=color, pos=pos)
        self.cars.append(car)


    def move_cars(self):
        for car in self.cars:
            car.move(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT