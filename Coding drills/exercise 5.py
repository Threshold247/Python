# Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them. Go to the editor


firstN = input("Enter your first name: ")
lastN = input("Enter your last name: ")

print(lastN, firstN)

# OR
# Complete reverse order

firstNa = input("Enter your first name: ")[::-1]
lastNa = input("Enter your last name: ")[::-1]
print(lastNa, firstNa)
