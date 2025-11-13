from turtle import Screen, Turtle
from snake import Snake
import random
import time

#defining screen
screen=Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

#snake varaibles
is_game_on = True
snake = Snake()


while is_game_on:
    snake.move_snake()
    screen.onkeypress(snake.turn_up, "w")
    screen.onkeypress(snake.turn_down, "s")
    screen.onkeypress(snake.turn_left, "a")
    screen.onkeypress(snake.turn_right, "d")
    screen.listen()
    screen.update()
    time.sleep(0.1)
    

screen.exitonclick()