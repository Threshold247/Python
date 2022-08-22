# Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user.

num = int(input("Enter a number: "))
numcheck = num % 2

if numcheck > 0:
    print("The number is odd")
else:
    print("The number is even")
