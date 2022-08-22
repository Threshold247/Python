# Write a Python program to check a dictionary is empty or not


mydict = {1: 'zero', 2: "two", 3: "three", 4: "four"}
mydict1 = {}


def dictTest(dict):
    if len(dict) > 0:
        for key, value in dict.items():
            print(key, value)
    else:
        print("Empty")


dictTest(mydict1)
dictTest(mydict)
