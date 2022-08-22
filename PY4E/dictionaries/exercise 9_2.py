count = {}
fname = input('Enter a file name: ')
fhand = open(fname)
for line in fhand:
    line = line.rstrip()
    if line.startswith("From"):
        # print(line)
        words = line.split()
        #print(words, len(words))
        if len(words) > 3:
            days = words[2]
            count[days] = count.get(days, 0) + 1

print(count)
