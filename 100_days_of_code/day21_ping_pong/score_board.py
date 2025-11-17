from turtle import Turtle

class ScoreBoard(Turtle):

    ALIGNMENT = "center"
    FONT =  ("Minecraftia", 50, "normal")

    def __init__(self, player):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        if player == 1:
            self.goto(-50, 200)
        else:
            self.goto(50, 200)
        self.write_score()
        
    def write_score(self):
        self.clear()
        self.write(arg=f"{self.score}",align=self.ALIGNMENT,font= self.FONT)
    
    def increase_score(self):
        self.score += 1
        self.write_score()