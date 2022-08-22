# Write a Python program to get the volume of a sphere with radius 6.
from math import pi


def sphere(rad):
    rad = float(rad)
    vol = (4/3)*pi*(rad**3)
    return print(vol)


sphere(3)
