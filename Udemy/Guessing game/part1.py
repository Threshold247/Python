# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
from art import logo
print(logo)


EASY_LVL = 10
HARD_LVL = 5


def compare(guess, answer, turns):
    """Checks guess against answer and reduces turns"""
    if guess > answer:
        print("Too High")
        return turns - 1
    elif guess < answer:
        print("Too low")
        return turns-1
    else:
        print(f"You guessed the correct number: {answer}")


def level():
    '''Generates turns based of difficulty'''
    select_level = input("Select easy or hard: ")
    if select_level == 'easy':
        return EASY_LVL
    else:
        return HARD_LVL


def game():
    turns = level()

    number_to_guess = random.randrange(0, 101)  # generate a randomn nuumber
    player_guess = 0
    while player_guess != number_to_guess:
        print(f"You have {turns} attempt(s)")
        # generate a user input
        player_guess = int(input('Guess a number between 1 and 100: \n'))
        # print(number_to_guess)
        turns = compare(guess=player_guess,
                        answer=number_to_guess, turns=turns)
        if turns == 0:
            print("No more turns left")
            print(f"The correct answer is {number_to_guess}")
            return


game()
