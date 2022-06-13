from turtle import Turtle, Screen
from prettytable import PrettyTable

bob = Turtle()  # if we were to import the whole library (turtle) we would have had to write bob = turtle.Turtle()
# bob = object
# Turtle() = class (blueprint)
print(bob)
bob.shape("turtle")
bob.color("Coral")  # these are the methods
bob.forward(100)


my_screen = Screen()
print(my_screen.canvheight)   # canvheight -> this is an  attribute of the screen
my_screen.exitonclick()

table = PrettyTable()  # installed a custom package called PrettyTable
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

table.align = "l"  # attribute that aligns the data from the table to the L - left

print(table)
