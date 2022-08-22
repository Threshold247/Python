#  Write a Python program to get the key, value and item in a dictionary
data = {'item1': 45.50, 'item2': 35, 'item3': 41.30, 'item4': 55, 'item5': 24}


print("key  value  count")
for count, (key, value) in enumerate(data.items(), 1):
    print(key, " ", int(value), " ", count)
