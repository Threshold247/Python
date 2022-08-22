# Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x)


n = int(input("Enter a number: "))
counts = {}

for x in range(1, n+1):  # sets how long the loop will run for
    print(x)
    counts.update({x: x*x})  # updates the dict with key and value
print(counts)
