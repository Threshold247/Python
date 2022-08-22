# Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary. Go to the editor
# Sample data : {'1':['a','b'], '2':['c','d']}

myDict = {'1': ['a', 'b'], '2': ['c', 'd']}

list1 = myDict['1']
list2 = myDict['2']

for i in list1:
    for j in list2:
        print(i+j)
