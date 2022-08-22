#  Write a Python program to calculate the hypotenuse of a right angled triangle
# z = square root of x squared + y squared
import math


def hypotenuse():
    a = (int(input("Enter a value for a: "))**2)
    b = (int(input("Enter a value for b: "))**2)
    sum = math.sqrt(a+b)
    print(round(sum, 2))


hypotenuse()
