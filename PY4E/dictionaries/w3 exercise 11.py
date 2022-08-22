# Write a Python program to multiply all the items in a dictionary.

mydict = {1: 20, 2: 30}
total = 1

for k, v in mydict.items():
    total *= v
print(total)

# OR

mydict1 = {2: 20, 3: 40}
result = 1

for keys in mydict1:
    result *= mydict1[keys]
print(result)
