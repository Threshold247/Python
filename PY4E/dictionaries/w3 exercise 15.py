#  Write a Python program to get the maximum and minimum value in a dictionary

mydict = {1: 'zero', 2: "two", 3: "three", 4: "four"}

print(max(mydict.items()))  # checks for max value in dictionary based on key
print(min(mydict.keys()))  # checks for min value of key in dictionary
print(min(mydict.values()))  # checks for min value of value in dictionary
