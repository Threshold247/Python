# Write a Python program to sort a given dictionary by key


from operator import itemgetter

mydict = {'blue': "two", 'green': "one", "red": "three"}
print(dict(sorted(mydict.items(), key=itemgetter(0))))
print(dict(sorted(mydict.items(), key=itemgetter(0), reverse=True)))

# OR
mydict1 = {'blue': "two", 'green': "one", "red": "three"}
for key in sorted(mydict1):
    print(("%s, %s" % (key, mydict1[key])))
