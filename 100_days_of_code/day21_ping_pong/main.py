from player_stick import PlayerStick
from ball import Ball
from score_board import ScoreBoard
from turtle import Screen

#initialize Screen and objects
screen = Screen()
screen.bgcolor("black")
screen.setup(600, 600)
score = ScoreBoard()
ball = Ball()
player_stick = PlayerStick()
computer_stick = PlayerStick()


screen.exitonclick()