# Write a Python program to compute the distance between the points (x1, y1) and (x2, y2)
import math


def distancecalc(x1, y1, x2, y2):
    p1 = [x1, y1]
    p2 = [x2, y2]
    # Distance formula is square root of (p1(x1)-p2(x2))**2+ p1(y1)-p2(y2)**2)
    distance = math.sqrt(((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2))
    return round(distance, 2)


print(distancecalc(4, 0, 6, 6))
