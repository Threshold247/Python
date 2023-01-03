

# Write your code above 👆
with open("file1.txt") as file1:
    file_data1 = file1.readlines()

with open("file2.txt") as file2:
    file_data2 = file2.readlines()

result = [int(number) for number in file_data1 if number in file_data2]
print(result)


