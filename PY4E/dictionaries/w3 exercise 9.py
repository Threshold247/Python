# Write a Python program to iterate over dictionaries using for loops

dict1 = {'one': 1}
dict2 = {'two': 2}
dict3 = {}


def iterate(*dict):
    for item in (dict):
        for k, v in item.items():
            print(k, ":", v)
        dict3.update(item)
        print(dict3)


iterate(dict1, dict2)
