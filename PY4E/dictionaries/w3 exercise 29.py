# Write a Python program to remove spaces from dictionary keys.

student_list = {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
print("Original dictionary: ",student_list)
result = {key.replace(" ","") :value for key, value in student_list.items()}
print(result)
