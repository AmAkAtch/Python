from turtle import Turtle

class PlayerStick(Turtle):

    def __init__(self, player):
        super().__init__()
        self.stick = []
        self.create_stick(player)
        

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
            
        