import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


player = Player()
level = Scoreboard()
car = CarManager()

def move_turtle_up():
    screen.onkeypress(player.move_up, "w")
    screen.listen()

def update_score():
    global sleep_time
    if player.ycor() >= 260:
        level.increase_level()
        player.reset_pos()

game_is_on = True

move_turtle_up()
while game_is_on:
    car.create_car()
    car.move_car()
    update_score()
    time.sleep(0.1)
    car.remove_offscreen_cars()
    screen.update()
