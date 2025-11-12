from turtle import Turtle, Screen
from turtle_model import TurtleModel
import random

screen = Screen()
screen.screensize(300, 200)

turtle_list = []
turtle_colors = ["red", "yellow", "green", "blue", "purple", "orange"]


def start_race():
    is_race_on = True
    while is_race_on:
        for turtle in turtle_list:
            turtle.forward(random.randint(0, 10))
            position = turtle.xcor()
            if position >= 300:
                is_race_on = False
                print(f"{turtle.pencolor()} wins the race")
                return turtle.pencolor().lower()
    
for turtle_number in range(-3, 3):
    turtle = Turtle()
    turtle.penup()
    turtle.shape("turtle")
    turtle.color(turtle_colors[turtle_number])
    turtle.goto(-300, turtle_number * 50)
    turtle_list.append(turtle)

user_bet = screen.textinput(title="Make a Bet",prompt="Please make a bet on a turtle: ").lower()
winner = screen.onkey(fun=start_race, key="Return")
screen.listen()

if winner == user_bet:
    print("Congrats you won the game..")
else:
    print(f"You suck, you guessed {user_bet}")



screen.exitonclick()