from turtle import Turtle
from typing import Tuple

class Car(Turtle):

    def __init__(self, color, pos: Tuple[float, float]):
        super().__init__()
        self.color(color)
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.setpos(pos)


    def move(self, distance):
        self.setpos(self.xcor() - distance, self.ycor())