# Write a Python program to create a dictionary from a string. Go to the editor
# Note: Track the count of the letters from the string.
from collections import Counter
data = 'w3resource'
count = {}
for letter in data:
    count[letter] = count.get(letter, 0)+1
print(count)

# OR

print(dict(Counter(data)))
