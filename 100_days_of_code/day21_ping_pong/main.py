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
    painter.width(5)
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

def update_score():
    if ball.xcor() <= -300:
        comp_score.increase_score()
        ball.reset_ball()
    elif ball.xcor() >= 300:
        p1_score.increase_score()
        ball.reset_ball()
 
def detect_bounce():
    if ball.ycor() <= -280 or ball.ycor() >= 280:
        ball.seth(360 - ball.heading()) 

def detect_collision_with_sticks():
    for segment in player_stick.stick + computer_stick.stick:
        if ball.distance(segment) < 20:
            ball.setheading(180 - ball.heading())

def move_player_stick():
    screen.onkeypress(player_stick.move_up, "w")
    screen.onkeypress(player_stick.move_down, "s")
    screen.listen()

is_game_on = True

draw_line()
while is_game_on:
    ball.move_ball()
    detect_bounce()
    move_player_stick()
    computer_stick.move_stick()
    detect_collision_with_sticks()
    update_score()
    screen.update()
    time.sleep(0.1)


screen.exitonclick()