# Write your code below this line 👇

def prime_checker(number):
    if number > 1:
        for item in range(2, number):
            if (number % item) == 0:
                print("Not a Prime Number")
                break
        else:
            print("Is a prime")

# Write your code above this line 👆


# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
