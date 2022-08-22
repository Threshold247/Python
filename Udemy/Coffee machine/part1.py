# create new hot flavours
from data import MENU, resources, coins


# TODO 1 Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
# TODO 2 Turn off the machine by typing off
# TODO 3 Print a report for the coffee machine

profit = 0


def insert_coins():
    '''Accepts coins and returns total'''
    quarters = float(input("Insert quarters: ")) * coins["quarters"]
    dimes = float(input("Insert dimes: ")) * coins["dimes"]
    nickles = float(input("Insert nickles: ")) * coins["nickles"]
    pennies = float(input("Insert pennies: ")) * coins["pennies"]
    total = quarters+dimes+nickles+pennies
    return(round(total, 2))


def check_ingredients(order_ingredients):
    """Checks if there are enough ingredients to process an order"""
    for item in order_ingredients:
        if resources[item] <= order_ingredients[item]:
            print(f"Sorry there is not enough {item}.")
            return False
        else:
            return True


def update_ingredients(order_ingredients):
    """Updates the ingredients after successful order processed"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]


ordering = True
while ordering:

    customer_input = input(
        f'What would you like? espresso/latte/cappuccino:').lower()
    if customer_input == 'report':
        print(
            f"water : {resources['water']}ml\nmilk : {resources['milk']}ml\ncoffee : {resources['coffee']}g\nmoney : ${profit}")
    elif customer_input == 'off':
        print("Shutting down")
        ordering = False
    else:
        # Access the dring from Menu after customer has chosen
        beverage = MENU[customer_input]
        # Access the ingredients for chosen drink
        if check_ingredients(beverage["ingredients"]):
            money = insert_coins()
            if money < beverage["cost"]:
                print("Not enough money. Money refunded")
            else:
                update_ingredients(beverage["ingredients"])
                profit += beverage["cost"]
                change = money-beverage['cost']
                rounded_change = round(change, 2)
                print(
                    f"Please take your {customer_input}. Your change is : ${rounded_change}")

   # Original Code
    # if customer_input == "latte" or customer_input == "cappuccino":
    #     my_coins = insert_coins()
    #     print(my_coins)
    #     if my_coins >= MENU[customer_input]['cost']:
    #         print(customer_input)
    #         if water < MENU[customer_input]['ingredients']['water']:
    #             print("Too little water")
    #             break
    #         if coffee < MENU[customer_input]['ingredients']['coffee']:
    #             print("Too little coffee")
    #             break
    #         if milk < MENU[customer_input]['ingredients']['coffee']:
    #             print("Too little milk")
    #             break
    #         else:
    #             water = water - MENU[customer_input]['ingredients']['water']
    #             coffee = coffee - MENU[customer_input]['ingredients']['coffee']
    #             milk = milk - MENU[customer_input]['ingredients']['milk']
    #             money = money + MENU[customer_input]['cost']
    #             print("Money:", money)
    #             print("Your change is:", round(
    #                 my_coins - MENU[customer_input]['cost'], 2))
    #             print("Please collect your coffee")
    #     else:
    #         print("Not enough money to buy the beverage")
    #         ordering = False
