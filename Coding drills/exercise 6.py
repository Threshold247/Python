# Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
# Sample data : 3, 5, 7, 23
# Output :
# List : ['3', ' 5', ' 7', ' 23']
# Tuple : ('3', ' 5', ' 7', ' 23')

values = (input("Input some comma seprated numbers : "))
list = values.split(",")
tup = tuple(list)
print('List : ', list)
print('Tuple : ', tuple)
nlist = []
# output is string format!

# convert to integer
for items in list:
    myitems = int(items)
    nlist.append(myitems)
print(nlist)
ntup = tuple(nlist)
print(ntup)
