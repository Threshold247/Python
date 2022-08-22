from art import logo
import os


print(logo)

auction_dict = {}

bid = True
while bid:

    bid_name = input("Enter name: \n")
    bid_value = int(input("Enter bid amount: \n"))

    auction_dict[bid_name] = bid_value

    decide = input("Done? Yes or No\n").lower()
    if decide == "yes":
        bid = False
    elif decide == "no":
        os.system('cls')

Largest = None

for items in auction_dict:
    if Largest is None:
        Largest = auction_dict[items]
    elif auction_dict[items] > Largest:
        Largest = auction_dict[items]

print(f"{items} won with the largest bid of {Largest}")
