#  Write a Python program to iterate over dictionaries using for loops.

mydict = {"timothy": 20, "joe": 30}
for k in mydict:
    print(k, mydict[k])
# OR
mydict1 = {"timothy": 20, "joe": 30}
for k, v in mydict1.items():
    print(k, v)
