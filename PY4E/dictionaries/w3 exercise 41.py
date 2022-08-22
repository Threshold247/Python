# Write a Python program to drop empty Items from a given Dictionary. Go to the editor
# Original Dictionary:
# {'c1': 'Red', 'c2': 'Green', 'c3': None}

data = {'c1': 'Red', 'c2': 'Green', 'c3': None}
d1 = {}
for keys, values in data.items():
    if values is not None:
        d1[keys] = values
print(d1)
