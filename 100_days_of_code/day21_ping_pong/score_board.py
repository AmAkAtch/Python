from turtle import Turtle

class ScoreBoard(Turtle):

    ALIGNMENT = "center"
    FONT =  ("Arial", 20, "normal")

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.write(arg=f"{self.score}",align=self.ALIGNMENT,font= self.FONT)