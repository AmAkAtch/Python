from turtle import Turtle, Screen

pointer = Turtle()
screen = Screen()
screen.listen()

def move_forward():
    pointer.forward(5)

def move_back():
    pointer.back(5)

def turn_rigth():
    pointer.right(5)

def turn_left():
    pointer.left(5)

def clear_screen():
    pointer.clear()

screen.onkeypress(fun=move_forward, key="w")
screen.onkeypress(fun=move_back, key="s")
screen.onkeypress(fun=turn_left, key="a")
screen.onkeypress(fun=turn_rigth, key="d")
screen.onkeypress(fun=clear_screen, key="c")


screen.exitonclick()