import re
total = 0
count = 0
fname = 'sumregex2.txt'
fhand = open(fname)

for lines in fhand:
    lines = lines.rstrip()
    # print(lines)
    check = re.findall('[0-9]+', lines)

    if not len(check) > 0:
        continue

    for items in check:
        numbers = float(items)
        count = count + 1
        total = total + numbers

print(count, total)
