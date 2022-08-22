# Write a Python program which accepts the radius of a circle from the user and compute the area.
# Sample Output :
# r = 1.1
# Area = 3.8013271108436504

from math import pi


def calcu():
    diameter = float(input("Enter a diameter: "))
    rad = (diameter**2)*pi
    return print(rad)


calcu()
