name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
text = open(name)

count = dict()

for line in text:
    line.rstrip()
    if not line.startswith("From "):
        continue
    # print(line)
    words = line.split()
    # print(words)
    count[words[1]] = count.get(words[1], 0)+1
print(count)

largestAu = None
largestEmail = None

for key, value in count.items():
    if largestAu is None:
        largestAu = value
    if largestAu < value:
        largestAu = value
        largestEmail = key

print(largestAu, largestEmail)
