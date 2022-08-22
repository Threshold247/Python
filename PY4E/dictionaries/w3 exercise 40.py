# Write a Python program to create a dictionary of keys x, y, and z where each key has as value a list from 11-20, 21-30, and 31-40 respectively. Access the fifth value of each key from the dictionary. Go to the editor
from pprint import pprint
data = dict(x=list(range(11, 20)), y=list(
    range(21, 30)), z=list(range(31, 40)))
pprint(data)
# for key, value in data.items():
#     print(f"{value[4]}")
# for k, v in data.items():
#     print(f"{k},{v}")
