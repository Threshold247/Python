# Write a Python program to count the values associated with key in a dictionary

# cannot count strings directly. have to add into a dictionary first

student = [{'id': 1, 'success': True, 'name': 'Lary'},
           {'id': 2, 'success': False, 'name': 'Rabi'},
           {'id': 3, 'success': True, 'name': 'Alex'}]

counter = 0
count = {}

print(sum(items['id'] for items in student))  # integer
print(sum(items['success'] for items in student))  # boolean


for items in student:
    result = items['name']
    count[result] = count.get(result, 0)+1
print(sum(count.values()))
