# Write a Python program to find the highest 3 values of corresponding keys in a dictionary.


from heapq import nlargest
data = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
largest = nlargest(3, data, key=data.get)
print(largest)

# OR
mylist = []
for key in data.keys():
    mylist.append(key)
print(sorted(mylist[2:5], reverse=True))
