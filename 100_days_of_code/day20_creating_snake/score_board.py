from turtle import Turtle

class ScoreBoard(Turtle):

    ALIGNMENT = "center"
    FONT = ("Arial", 20, "normal")

    def __init__(self):
        super().__init__()
        self.current_score = -1
        self.high_score = 0
        self.display_score()

    def display_score(self):
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        self.refresh_score()
    
    def refresh_score(self):
        self.current_score += 1
        self.clear()
        self.write(arg=f"Score: {self.current_score} High Score: {self.high_score}", align=self.ALIGNMENT, font=self.FONT)

    def reset(self):
        if self.current_score > self.high_score:
            self.high_score = self.current_score
        self.current_score = -1
        self.refresh_score()

    # def game_over(self):
    #     self.color("white")
    #     self.goto(0,0)
    #     self.write("GAME OVER", align=self.ALIGNMENT, font=self.FONT)