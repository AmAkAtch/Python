from turtle import Turtle

class Snake:
    def __init__(self):
        self.snake_body = []
        self.initial_position = [(0,0), (-20,0), (-40,0)]
        self.define_snake()
    
    def define_snake(self):
        for seg_pos in self.initial_position:
            self.add_segment(seg_pos)
            self.snake_head = self.snake_body[0]

    def add_segment(self, seg_pos):
        snake=Turtle()
        snake.penup()
        snake.color("white")
        snake.shape("square")
        snake.setpos(seg_pos)
        self.snake_body.append(snake)

    def move_snake(self):
        for seg_index in range(len(self.snake_body)-1, 0,-1):
            x_cor = self.snake_body[seg_index-1].xcor()
            y_cor = self.snake_body[seg_index-1].ycor()
            self.snake_body[seg_index].goto(x_cor, y_cor)
        self.snake_head.forward(20)
    
    def snake_reset(self):
        for snake in self.snake_body:
            snake.hideturtle()
        self.snake_body.clear()
        self.define_snake()


    def turn_up(self):
        if self.snake_body[0].heading() == 0 or self.snake_body[0].heading()==180:
            self.snake_body[0].seth(90)

    def turn_left(self):
        if self.snake_body[0].heading() == 90 or self.snake_body[0].heading()==270:
            self.snake_body[0].seth(180)

    def turn_right(self):
        if self.snake_body[0].heading() == 90 or self.snake_body[0].heading()==270:
            self.snake_body[0].seth(0)

    def turn_down(self):
        if self.snake_body[0].heading() == 0 or self.snake_body[0].heading()==180:
            self.snake_body[0].seth(270)