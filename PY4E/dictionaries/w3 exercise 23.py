#  Write a Python program to combine values in python list of dictionaries

from collections import Counter
Sampledata = [{'item': 'item1', 'amount': 400}, {
    'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
mydict = {}
result = Counter()
for items in Sampledata:
    result[items['item']] += items['amount']
print(result)
