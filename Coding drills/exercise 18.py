# Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum


x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
z = int(input("Enter the third number: "))
mysum = (x+y+z)
if x == y == z:
    print((mysum)*3)
else:
    print(mysum)
