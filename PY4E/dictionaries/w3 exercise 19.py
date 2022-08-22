# Write a Python program to combine two dictionary adding values for common keys

from collections import Counter
d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}
d3 = {}

d3.update(d1)
d3.update(d2)

for key, value in d1.items():  # loop through dictionary 1
    for keys, values in d2.items():  # loop through dictionary 2
        if key == keys:  # if the keys are the same for dict 1 and 2
            # then add the values of each key from each dictionary (dict1 and dict 2)
            d3[key] = value+values
print(d3)

# OR


d3 = Counter(d1) + Counter(d2)
print(d3)
for key, value in d3.items():
    print(key, value)
