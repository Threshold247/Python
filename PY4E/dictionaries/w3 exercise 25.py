# Write a Python program to print a dictionary in table format

data = {'C1': [1, 2, 3], 'C2': [5, 6, 7], 'C3': [9, 10, 11]}

print(*list(data.keys()))
a = (list(data.values()))
for i in range(len(a)):
    print(*(a[i]))

# OR

for items in zip(*([key]+(value) for key, value in sorted(data.items()))):
    print(*items)
