# 🚨 Don't change the code below 👇


print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
name3 = (name1+name2).lower()

T = name3.count("t")
R = name3.count("r")
U = name3.count("u")
E = name3.count("e")

L = name3.count("l")
O = name3.count("o")
V = name3.count("v")
E = name3.count("e")


total1 = T+R+U+E
total2 = L+O+V+E

total_str = str(total1)+str(total2)
total3 = int(total_str)
print(total3)

if total3 < 10 or total3 > 90:
    print(f"Your score is {total3}, you go together like coke and mentos.")
elif total3 >= 40 and total3 <= 50:
    print(f"Your score is {total3}, you are alright together.")
else:
    print(f"Your score is {total3}")
