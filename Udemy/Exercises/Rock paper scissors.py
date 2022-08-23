import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
pc_list = ["rock", "paper", "scissors"]

pc_choice = pc_list[random.randint(0, 2)-1]
print(pc_choice)

user_choice = input("Choose either Rock, Paper or Scissors: \n")
user_choice_convert = user_choice.lower()
print(user_choice_convert)

if pc_choice == "rock":
    if user_choice_convert == "scissors":
        print(f"Computer chose {rock}, the User chose {scissors}. User loses")
    elif user_choice_convert == "paper":
        print(f"Computer chose {rock}, the User chose {paper}. User wins")
    else:
        print("draw")
elif pc_choice == "paper":
    if user_choice_convert == "scissors":
        print(f"Computer chose {paper}, the User chose {scissors}. User wins")
    elif user_choice_convert == "rock":
        print(f"Computer chose {paper}, the User chose {rock}. User loses")
    else:
        print("draw")
elif pc_choice == "scissors":
    if user_choice_convert == "scissors":
        print("Draw")
    elif user_choice_convert == "rock":
        print(f"Computer chose {scissors}, the User chose {rock}.User wins")
    else:
        print(f"Computer chose {scissors}, the User chose {paper}. User loses")
