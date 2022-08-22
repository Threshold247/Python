fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0

for line in fh:
    email = line.split()
    if len(email) == 0:
        continue
    if email[0] != "From":
        continue
    count += 1
    print(email[1])
print("There were", count, "lines in the file with From as the first word")
