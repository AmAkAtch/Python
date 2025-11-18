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
        car.increase_move_distance()

def detect_collision():
    global game_is_on
    for cars in car.all_cars:
        if cars.distance(player) <30 and cars.xcor()-20<=player.xcor() <= cars.xcor()+20 :
            level.game_over()
            game_is_on = False

game_is_on = True

move_turtle_up()
while game_is_on:
    update_score()
    car.create_car()
    car.move_car()
    detect_collision()
    time.sleep(0.1)
    car.remove_offscreen_cars()
    screen.update()

screen.exitonclick()