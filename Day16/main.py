# # object oriented programming
#
# from turtle import Turtle, Screen
# # import turtle
#
# # created object of the class Turtle
# # timmy = turtle.Turtle()
# donny = Turtle()
# print(donny)
# donny.shape("turtle")
# donny.color("Coral")
# donny.forward(100)
#
# # canvheight is an attribute of class Screen. Attributes are nothing but variables in the class.
# my_screen = Screen()
# print(my_screen.canvheight)
#
# # exitonclick is a method of class Screen. Methods are nothing but functions in the class.
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon", ["Pikachu", "Charmander", "Squirtle", "Bulbasaur", "Gastly"])
table.add_column("Type", ["Thunder", "Fire", "Water", "Grass", "Ghost"])
table.align = 'l'
print(table.align)
print(table)

