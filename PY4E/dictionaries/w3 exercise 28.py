# Write a Python program to sort a list alphabetically in a dictionary


myDict = {"a": ["Joe", "Brock", "cat"], "b": [
    "dog", "Banana"], "c": ["Orange", "Apple"]}

for key in myDict:  # go through dictionary
    print("Original keys", key)
    print("Original values", myDict[key])
    print("Sorted Values", sorted(myDict[key]))
    # bring back the value of each key and sorted it then store it as the new value.
    myDict[key] = sorted(myDict[key])
print(myDict)
# OR
result = {keys: sorted(values) for keys, values in myDict.items()}
print(result)
