# Write a Python program to count number of items in a dictionary value that is a list.

data = {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}

for key, value in data.items():
    print(key, len(value))

# or

result = sum(map(len, data.values()))  # map requires 2 arguments
print(result)
