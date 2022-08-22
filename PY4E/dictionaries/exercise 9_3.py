count = {}

fhand = open('mbox-short.txt')

for line in fhand:
    line = line.strip()
    # Finds lines beginning with From
    if line.find("From "):
        continue
    # Split lines
    words = line.split()
    # Store word into email variable
    email = words[1]
    # Adds all emails to the dictionary
    count[email] = count.get(email, 0) + 1
print(count)
