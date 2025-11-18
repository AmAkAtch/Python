from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.color("black")
        self.penup()
        self.goto(-280,260)
        self.hideturtle()
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(arg=f"Level: {self.level}", align="left", font=FONT)
    
    def increase_level(self):
        self.level += 1
        self.write_score()

    def game_over(self):
        self.goto(0,0)
        self.write(arg="Game Over", align="center", font=FONT)
