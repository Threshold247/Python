from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


my_money = MoneyMachine()
my_coffee = CoffeeMaker()
my_menu = Menu()

is_on = True


while is_on:

    choice = input(f"Choose a beverage:{my_menu.get_items()}\n")

    if choice == "off":
        print("Shutting down")
        is_on = False
    elif choice == "report":
        my_coffee.report()
        my_money.report()
    else:
        drink = my_menu.find_drink(choice)
        if my_coffee.is_resource_sufficient(drink) and my_money.make_payment(drink.cost):
            my_coffee.make_coffee(drink)





