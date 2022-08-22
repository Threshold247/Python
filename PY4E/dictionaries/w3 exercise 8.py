# Write a Python script to merge two Python dictionaries

dict1 = {'one': 1, 'two': 2}
dict2 = {'x': 2, 'y': 3}
mydict = dict2 | dict1
print(mydict)

# OR


def merge(*dict):  # Very important * allows for additonal arguments
    newdict = {}
    for items in dict:
        newdict.update(items)
    return newdict


print(merge(dict1, dict2))
