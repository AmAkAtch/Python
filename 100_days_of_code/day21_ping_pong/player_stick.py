from turtle import Turtle

class PlayerStick(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.seth(90)
        self.setpos(-280, 0)
        
        