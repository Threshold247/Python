obj = dict()
count = 0
fname = open('words.txt')
for line in fname:
    words = line.split()
    print(words)
    for word in words:
        count += 1         #counts the words
        if word in obj:    #Discards teh duplicate words
            continue
        obj[word] = count  # Value is first time word appears
print(obj)