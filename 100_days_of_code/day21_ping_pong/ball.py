from turtle import Turtle
import random
class Ball(Turtle):

    ANGLE = random.uniform(0, 360)
    
    def __init__(self):
        super().__init__()
        self.create_ball()

    def create_ball(self):
        self.color("white")
        self.shape("circle")
        self.penup()
        self.setheading(self.ANGLE)
        if self.ANGLE == 270 or self.ANGLE == 90:
            self.setheading(20)
        self.move_ball()

    def reset_ball(self):
        self.ANGLE = random.uniform(0, 360)
        self.seth(self.ANGLE)
        self.setpos(0,0)

    def move_ball(self):
        self.forward(10)