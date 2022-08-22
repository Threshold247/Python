capture = 0

for number in range(0, 101):
    if number % 2 == 0:
        capture = capture+number
print(capture)


#OR
total = 0
for item in range(0,101,2):
    total = total + item
print(total)
