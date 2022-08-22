from art import logo, vs
from game_data import data
import random
import os


def format_data(account):
    '''Access value of the given key from the dictionary. Takes an argument of dictionary'''
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, {account_description} from {account_country}"


def compare_guess(player_choice, com_choice):
    """Compares choice against computer"""
    if player_choice > com_choice:
        return True
    else:
        return False


# Import art
print(logo)
score = 0
# Generate randomn data
sample2 = random.choice(data)

# Create a While loop
guessing = True
while guessing:

    # The game requires 2nd guessing option to become 1st guessing option when it loops
    sample1 = sample2
    sample2 = random.choice(data)
    # while sample1 == sample 2 then the game will choose another random account
    while sample1 == sample2:
        sample2 = random.choice(data)

    # Format the data
    print(f'Compare A: {format_data(sample1)}')

    # Import art
    print(vs)

    print(f'Versus B: {format_data(sample2)}')

    player_choice = input("Who has more followers? 'A' or 'B' \n").lower()
    com_choice = ''

    if player_choice == 'a':
        player_choice = sample1["follower_count"]
        com_choice = sample2["follower_count"]
    if player_choice == 'b':
        player_choice = sample2["follower_count"]
        com_choice = sample1["follower_count"]

    print(player_choice)
    print(com_choice)

    os.system('cls')
    print(logo)
    is_correct = compare_guess(player_choice, com_choice)
    if is_correct == True:
        score += 1
        print(f"You are correct. Your current score is {score}\n")
    else:
        guessing = False
        print(f"You are incorrect. Your final score is {score}")
