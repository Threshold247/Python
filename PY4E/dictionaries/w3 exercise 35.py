# Write a Python program to sort Counter by value.
# Sample data : {'Math':81, 'Physics':83, 'Chemistry':87}
# Expected data: [('Chemistry', 87), ('Physics', 83), ('Math', 81)]

from operator import itemgetter
from collections import Counter


data = {'Math': 81, 'Physics': 83, 'Chemistry': 87}

myDict = dict(sorted(data.items(), key=itemgetter(1), reverse=True))
print(myDict)
newList = list(myDict.items())
print(newList)

# Or

myList = Counter((data))
print(myList.most_common())
