# Write a Python script to sort (ascending and descending) a dictionary by value

import operator

data = ['one', 'two', 'three', 'two', 'three', 'three']
count = {}

for item in data:
    count[item] = count.get(item, 0)+1
# sort dictionary by key in ascending order. adding "dict" converts output to dictionary
print("Sort dictionary by key in ascending order",
      dict(sorted(count.items(), key=operator.itemgetter(0))))
# sort dictionary by key in descending order
print(dict(sorted(count.items(), key=operator.itemgetter(0), reverse=True)))
# sort dictionary by value in ascending order
print(dict(sorted(count.items(), key=operator.itemgetter(1))))
# sort dictionary by value in descending order
print(dict(sorted(count.items(), key=operator.itemgetter(1), reverse=True)))
