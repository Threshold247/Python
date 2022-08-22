# Write a Python program to replace dictionary values with their average


data = [{'id': 1, 'subject': 'math', 'V': 70, 'VI': 82},
        {'id': 2, 'subject': 'math', 'V': 73, 'VI': 74},
        {'id': 3, 'subject': 'math', 'V': 75, 'VI': 86}]


def myAvg(listOfDict):  # Only works when using a list
    for items in listOfDict:
        n1 = items.pop('V')  # for each item, remove the key V
        print(n1)
        n2 = items.pop('VI')  # for each item, remove the key VI
        print(n2)
        items['V+VI'] = (n1+n2)/2  # use the value associated with each key and divide it by 2
    return listOfDict


print(myAvg(data))
