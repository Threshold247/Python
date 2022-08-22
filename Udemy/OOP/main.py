# from turtle import Turtle, Screen
#
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("chartreuse1")
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# my_screen = Screen()
#
# # print(my_screen.canvheight)
# # print(my_screen.canvwidth)
#
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon name",["Pikachu","Squirtle","Charmander"]), table.add_column("Type",["Electric","Water","Fire"])

table.align ="l"

print(table)