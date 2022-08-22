#  Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys

def createDict():
    myDict = {}
    n = int(input("Enter a number: "))
    for x in range(1, n+1):
        myDict[x] = x**2
    return myDict


print(createDict())
