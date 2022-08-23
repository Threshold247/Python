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

# from prettytable import PrettyTable

# table = PrettyTable()
# table.add_column("Pokemon name",["Pikachu","Squirtle","Charmander"]), table.add_column("Type",["Electric","Water","Fire"])

# table.align ="l"

# print(table)

class User:

    def __init__(self, id, user):
        self.user_id = id
        self.user_name = user
        self.followers = 0
        print(f"constructed {id} {user} has {self.followers} followers")

    def add_followers(self):
        self.followers += 1
        print(f"{self.user_id} {self.user_name} now has {self.followers} followers")

user_1 = User(1, "Jimbo")
user_2 = User(2, "Jill")

user_1.add_followers()
user_2.add_followers()



