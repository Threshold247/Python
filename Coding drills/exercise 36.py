# Write a Python program to add two objects if both objects are an integer type

def sumint(a, b):
    if type(a) == int and type(b) == int:
        return(a+b)
    else:
        return("One of the values is not an integer")


print("example 1: ", sumint(1, 2))
print("example 2: ", sumint(2, '3'))

# OR


def mytest(x, y):
    if isinstance(x, int) and isinstance(y, int):
        print(x+y)
    else:
        print("One of the values is not an integer")


mytest(1, 2)
mytest(1, "2")
