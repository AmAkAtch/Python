from turtle import Turtle, Screen
import random

turtle = Turtle()
turtle_colors = [
    "white", "black", "red", "green", "blue", "yellow", "cyan", "magenta",
    "gray", "orange", "purple", "brown", "pink", "gold", "silver", "navy",
    "maroon", "olive", "teal", "lime", "skyblue", "turquoise", "salmon",
    "coral", "orchid", "plum", "indigo", "violet", "tan", "beige", "chocolate",
    "crimson", "darkgreen", "darkblue", "darkred", "lightblue", "lightgreen",
    "lightgray", "lavender", "thistle", "tomato", "wheat", "seashell", "snow"
]
#Each shape has same sides and same angles

for sides in range (3, 11):
    turtle.color(random.choice(turtle_colors))
    for side in range(sides):
        turtle.forward(100)
        angle = (sides-2)*180/sides
        turtle.right(180-angle)


screen = Screen()
screen.exitonclick()

