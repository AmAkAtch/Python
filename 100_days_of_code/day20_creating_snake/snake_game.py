from turtle import Screen, Turtle
import random

#defining screen
screen=Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake Game")


#snake varaibles
head_pos_x = 0
head_pos_y = 0
body_count = 3
snake_body = []

#defining snake
for body in range(body_count):
    snake=Turtle()
    snake.color("white")
    snake.shape("square")
    snake.setpos(head_pos_x + (body*20), head_pos_y)





screen.exitonclick()