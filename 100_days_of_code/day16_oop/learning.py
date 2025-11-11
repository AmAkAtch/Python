from turtle import Turtle, Screen
from prettytable import PrettyTable

# timmy = Turtle()
# timmy.color("red")
# timmy.shape("turtle")
# print(timmy)

# my_screen = Screen()
# my_screen.exitonclick()

table = PrettyTable()

table.add_column("Pokemon",["pikachu", "Cobblemon"])
print(table)
table.add_column("Type", ["lightning", "Water"])
print(table)