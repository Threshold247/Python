# Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference.

num = int(input("Enter a number: "))
if num > 17:
    print(abs(17-num)*2)
else:
    print(17-num)
