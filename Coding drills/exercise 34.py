# Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20

def sum(a, b):
    mysum = a+b
    if mysum >= 15 and mysum <= 20:
        print(20)
    else:
        print(mysum)


sum(1, 2)
sum(12, 4)
sum(13, 8)

#OR

def testsum(a,b):
    mysum = a+b
    if mysum in range(15,20):
        print(20)
    else:
        print(mysum)


sum(1, 2)
sum(12, 4)
sum(13, 8)