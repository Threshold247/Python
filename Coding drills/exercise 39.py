# Write a Python program to compute the future value of a specified principal amount, rate of interest, and a number of years.
# Test Data : amt = 10000, int = 3.5, years = 7
# Expected Output : 12722.79

def interest_rate(amt, interest, time):
    return round(amt*((1+(0.01*interest))**time), 2)
# round off to 2 places


print(interest_rate(10000, 3.5, 7))
