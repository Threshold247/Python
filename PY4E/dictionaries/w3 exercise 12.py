#  Write a Python program to remove a key from a dictionary

mydict = {'a': 20, 'b': 30}

mydict.pop('a')
print(mydict)

# OR


count = {1: 20, 2: 30}


def delete(dict):
    inp = int(input("Enter a key: "))
    if inp in dict:
        del dict[1]
    print(dict)


delete(count)
