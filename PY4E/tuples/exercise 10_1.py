fname = input("Enter file: ")
if len(fname) < 1:
    fname = 'mbox-short.txt'
fhand = open(fname)
mydict = {}

for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
    mydict[words[1]] = mydict.get(words[1], 0) + 1


mylist = list()
for email, count in mydict.items():
    data = (count, email)
    mylist.append(data)
    mylist = sorted(mylist, reverse=True)
    print(mylist)
    

for count, email in mylist[:1]:
    print(email, count)
