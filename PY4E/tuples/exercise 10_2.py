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
    time = words[5]
    hours = time.split(':')
    mydict[hours[0]] = mydict.get(hours[0], 0)+1

mylist = list()
for k, v in mydict.items():
    mylist.append((k, v))
    mylist = sorted(mylist)
print(mylist)
for k, v in mylist:
    print(k, v)
