from turtle import Screen, Turtle
from snake import Snake
from food import Food
from score_board import ScoreBoard
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
food = Food()
score_board = ScoreBoard()

def detect_collision_with_food():
    if food.distance(snake.snake_head) <= 16:
        food.spawn_food()
        seg_pos = snake.snake_body[-1].pos()
        snake.add_segment(seg_pos)
        score_board.refresh_score()

def detect_collision_with_wall():
    if snake.snake_head.xcor() >= 280 or snake.snake_head.ycor() >= 280:
        score_board.game_over()
        global is_game_on
        is_game_on = False

def detect_collision_with_tail():
    for segment in snake.snake_body[1:]:
        if snake.snake_head.pos() == segment.pos():
            score_board.game_over()
            global is_game_on
            is_game_on = False

def detect_collision():
    detect_collision_with_food()
    detect_collision_with_wall()
    detect_collision_with_tail()

while is_game_on:
    snake.move_snake()
    screen.onkeypress(snake.turn_up, "w")
    screen.onkeypress(snake.turn_down, "s")
    screen.onkeypress(snake.turn_left, "a")
    screen.onkeypress(snake.turn_right, "d")
    detect_collision()
    screen.listen()
    screen.update()
    time.sleep(0.1)
    

screen.exitonclick()