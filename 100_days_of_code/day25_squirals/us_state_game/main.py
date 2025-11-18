import pandas as pd
from turtle import Turtle, Screen

screen = Screen()
screen.addshape("day25_squirals/us_state_game/blank_states_img.gif")

turtle = Turtle()
turtle.shape("day25_squirals/us_state_game/blank_states_img.gif")

state_names = pd.read_csv("day25_squirals/us_state_game/50_states.csv")
guessed_states = []

writer = Turtle()
writer.hideturtle()
writer.penup()

def check_answer(user_answer):
    global correct_guesses
    match = state_names[state_names["state"].str.lower() == user_answer.lower()]
    if not match.empty:
        if user_answer not in guessed_states:
            x_cor = int(match["x"])
            y_cor = int(match["y"])
            write_at_cords(x_cor, y_cor, user_answer)
            correct_guesses += 1
            guessed_states.append(user_answer)
            
def write_at_cords(x,y,name):
    writer.goto(x,y)
    writer.write(arg=name, align="center", font=("Arial", 8, "normal"))


is_game_on = True
correct_guesses = 0

while correct_guesses < 50:
    user_answer = screen.textinput(title=f"{correct_guesses} out of 50 Right Guesses", prompt="Enter US state Name").lower()
    check_answer(user_answer)

screen.mainloop()