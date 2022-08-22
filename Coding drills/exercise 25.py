# Write a Python program to check whether a specified value is contained in a group of values

def test(x, num):
    if num in x:
        print(True)
    else:
        print(False)


test([1, 5, 8, 3], 20)
