# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Write your code below this line 👇
bill = input("What is the total for the bill? \n")
add_tip = input("Enter a tip amount 10 ,12 or 15 \n")
people = input("Enter amount of people to split bill \n")


convert_bill = float(bill)
convert_tip = int(add_tip)
people = int(people)
tip_perc = convert_tip/100
total_bill = convert_bill + (convert_bill*tip_perc)
# format value to 2 decimal places.
people_split = "{:.2f}".format(total_bill/people)
print(people_split)
