import turtle
import colorgram
import random

colors = colorgram.extract("referance.jpg", 10)
turtle.colormode(255)

rows = 2
columns = 3

pointer = turtle.Turtle()
pointer.pensize(20)

for row in range(rows):
    for colum in range(columns):
        pointer.color(random.choice(colors).rgb)
        pointer.forward(1)
        pointer.penup()
        pointer.forward(29)
        pointer.pendown()

    pointer.penup()
    pointer.left(90)
    pointer.forward(29)
    pointer.right(90)
    pointer.back(30*columns)
    pointer.pendown()









screen = turtle.Screen()
screen.exitonclick()