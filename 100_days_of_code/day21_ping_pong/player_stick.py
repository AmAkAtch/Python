from turtle import Turtle, Screen

class PlayerStick(Turtle):

    def __init__(self, player):
        super().__init__()
        self.stick = []
        self.create_stick(player)
        self.stick_head = self.stick[0]
        self.screen = Screen()   
        

    def create_segment(self, seg_pos):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.seth(90)
        new_segment.setpos(seg_pos)
        self.stick.append(new_segment)

    def create_stick(self, player):
        if player == 1:
            positions = [(-270,20), (-270,0), (-270, -20)]
            for seg_pos in positions:
                self.create_segment(seg_pos)      
        else:
            positions = [(270,20), (270,0), (270, -20)]
            for seg_pos in positions:
                self.create_segment(seg_pos)
             
    def move_stick(self):
        if self.stick_head.ycor() >= 280:
            self.stick_head.seth(-90)
            self.stick_head.forward(40)
        if self.stick_head.ycor() <= -280:
            self.stick_head.seth(90)
            self.stick_head.forward(20)
        else:
            for seg_index in range(len(self.stick)-1, 0, -1):
                x_cor = self.stick[seg_index-1].xcor()
                y_cor = self.stick[seg_index-1].ycor()
                self.stick[seg_index].goto(x_cor, y_cor)
            self.stick_head.forward(20)

    def move_up(self):
        self.stick_head.seth(90)
        if self.stick_head.ycor() <= 280:
            self.move_entire_stick()
            self.stick_head.forward(10)

    def move_down(self):
        self.stick_head.seth(-90)
        if self.stick_head.ycor() >= -280:
            self.move_entire_stick()
            self.stick_head.forward(10)

    def move_entire_stick(self):
        for seg_index in range(len(self.stick)-1, 0, -1):
                x_cor = self.stick[seg_index-1].xcor()
                y_cor = self.stick[seg_index-1].ycor()
                self.stick[seg_index].goto(x_cor, y_cor)