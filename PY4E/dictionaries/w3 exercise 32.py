# Write a Python program to print a dictionary line by line

students = {'Alex': {'class': 'V',
                     'rolld_id': 2},
            'Puja': {'class': 'V',
                     'roll_id': 3}}

for a in students:
    print(students[a])
    for b in students[a]:
        print(b, ":", students[a][b])
# OR

for key, values in students.items():
    print(key)
    for x, y in values.items():
        print(x, ":", y)
