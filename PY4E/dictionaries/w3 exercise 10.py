#  Write a Python program to sum all the items in a dictionary

my_dict = {'data1': 100, 'data2': -54, 'data3': '247', 'data4': 26}
total = 0
for value in my_dict.values():
    if type(value) == str:
        print(f"Error found string, {value}")
        break
    if type(value) != str:
        total = total + value
    print(total)
