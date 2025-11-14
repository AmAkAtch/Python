from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.spawn_food()

    def spawn_food(self):
        self.shape("circle")
        self.color("red")
        self.penup()
        self.goto(random.randint(-250, 250), random.randint(-250, 250))
    
   
    