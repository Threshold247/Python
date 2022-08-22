# Write a Python program to match key values in two dictionaries. Go to the editor
# Sample dictionary: {'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}
# Expected output: key1: 1 is present in both x and y

data1 = {'key1': 1, 'key2': 3, 'key3': 2}
data2 = {'key1': 1, 'key2': 2}

for items in data1.items():  # loop through 1st dictionary
    for item in data2.items():  # loop through 2nd dictionary
        if items == item:  # if both k,v of 1st dictionary == k,v of 2 dictionary
            print(f"{items[0]}: {items[1]} are in both data1 and data2")

# OR

for (key, values) in set(data1.items()) & set(data2.items()):
    print('%s: %s is present in both data1 and data2' % (key, values))
