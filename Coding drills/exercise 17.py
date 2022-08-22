#  Write a Python program to test whether a number is within 100 of 1000 or 2000.

number = int(input("Entert a numer to check: "))

if number <= 100:
    print("Within 100")
elif number <= 1000:
    print("Within 1000")
elif number <= 2000:
    print("Within 2000")
else:
    print("Number out of range")
