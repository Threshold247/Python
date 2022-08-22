#  Write a Python program to convert height (in feet and inches) to centimeters


feet = int(input("Enter feet: "))
inches = int(input("Enter inches: "))
conversion = feet*30.48 + inches * 2.54
print("The height is:", conversion, "centimeters")
