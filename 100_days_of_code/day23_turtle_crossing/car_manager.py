from turtle import Turtle
from random import choice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(choice(COLORS))
        self.shapesize(stretch_len=2)
        self.penup()
        self.goto(300,0)
        self.seth(180)

    def move_car(self):
        self.forward(STARTING_MOVE_DISTANCE)

    def increase_speed()

