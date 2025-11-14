from player_stick import PlayerStick
from ball import Ball
from score_board import ScoreBoard
from turtle import Screen, Turtle
import time

#initialize Screen and objects
screen = Screen()
screen.bgcolor("black")
screen.setup(600, 600)
screen.tracer(0)

p1_score = ScoreBoard(1)
comp_score = ScoreBoard(2)
player_stick = PlayerStick(1)
computer_stick = PlayerStick(2)
ball = Ball()

def draw_line():
    painter = Turtle("square")
    painter.hideturtle()
    painter.width(10)
    painter.penup()
    painter.color("white")
    painter.setpos(0, -300)
    painter.seth(90)
    for interation in range(10):
        painter.pendown()
        painter.forward(40)
        painter.penup()
        painter.forward(20)
    screen.update()

is_game_on = True

draw_line()
while is_game_on:
    ball.move_ball()
    screen.update()
    time.sleep(0.1)


screen.exitonclick()