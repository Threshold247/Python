#  Write a Python program to sum of three given integers. However, if two values are equal sum will be zero

def numbers(a, b, c):
    if a == b or a == c or b == c:
        print(0)
    else:
        print(a + b + c)


numbers(1, 2, 3)
numbers(1, 2, 2)
