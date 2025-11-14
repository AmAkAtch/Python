from turtle import Turtle
import random
class Ball(Turtle):

    ANGLE = random.uniform(0, 360)
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.setheading(self.ANGLE)
        self.move_ball()

    def move_ball(self):
        self.forward(10)