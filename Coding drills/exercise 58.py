# Write a Python program to sum of the first n positive integers.

def mytest():
    n = int(input("Enter a number: "))
    start = int(input("Enter a start position: "))
    mysum = sum(range(start, n+1))
    print(mysum)


mytest()
