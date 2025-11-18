from turtle import Turtle
from random import randint, choice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.all_cars = []
        self.current_move_distance = STARTING_MOVE_DISTANCE
        
    def create_car(self):
        if randint(1, 6) == 1:
            car = Turtle()
            car.shape("square")
            car.color(choice(COLORS))
            car.shapesize(stretch_len=2)
            car.penup()
            car.goto(300,randint(-200,200))
            car.seth(180)
            self.all_cars.append(car)
        

    def move_car(self):
        for car in self.all_cars:
            car.forward(self.current_move_distance)

    def remove_offscreen_cars(self):
        self.all_cars = [car for car in self.all_cars if car.xcor() > -320]

    def increase_move_distance(self):
        self.current_move_distance += MOVE_INCREMENT
