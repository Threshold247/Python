count = 0
total = 0
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    # print(line)
    pos = line.find(':')
    # print(pos)
    splitLine = line[pos+1:]
    # print(splitLine)
    stripLine = splitLine.strip()
    print(stripLine)
    number = float(stripLine)
    print(number)
    count = count + 1
    total = total + number
    # print(count, total)
print("Average spam confidence:", total/count)
print("Done")
