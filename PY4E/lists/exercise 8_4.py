name = input("Enter file name: ")
fh = open('romeo.txt')
lst = list()
count = 0
for line in fh:
    words = line.split()  # Splits senternce into words
    for word in words:
        if word in lst:   # Checks if word appears in list
            continue
        print(word)
        lst.append(word)  # Adds each word to list if it is not in the list
        lst.sort()        # sorts lists alphabetically
print(lst)
