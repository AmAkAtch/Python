from turtle import Turtle, Screen, colormode
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
#draw shapes from triangle to any number
def draw_shapes(number_of_shapes):
    for sides in range (3, number_of_shapes+1):
        turtle.color(random.choice(turtle_colors))
        for side in range(sides):
            turtle.forward(100)
            angle = (sides-2)*180/sides
            turtle.right(180-angle)

#draw random walk
def draw_random_walk(turns):
    for turn in range(turns):
        colormode(255)
        turtle.color(random.randint(0,255), random.randint(0,255),random.randint(0,255))
        turtle.pensize(5)
        turtle.forward(30)
        angle = random.randint(1,4)*90
        turtle.right(angle)


def draw_spirograph(turns):
    turtle.speed("fastest")
    for turn in range(turns):
        colormode(255)
        turtle.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        turtle.circle(100)
        turtle.right(360/turns)
        turtle.forward(5)

# draw_shapes(5)
# draw_random_walk(100)
draw_spirograph(200)


screen = Screen()
screen.exitonclick()

