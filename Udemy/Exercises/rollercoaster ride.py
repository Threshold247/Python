print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("What is your age? "))
bill = 0
want_photo = 0
if height >= 120:

    if age == 12:
        bill = 5
        # print("ticket price is R5")
    elif age < 18:
        bill = 10
        # print("ticket price is R10")
    else:
        bill = 15
        # print("ticket price is R15")
    want_photo = input("Do you want a photo? Y or N: ")
    if want_photo == "Y" or want_photo == "y":
        bill += 5
    print(bill)
else:
    print("Too short to ride")
