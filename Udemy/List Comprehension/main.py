# numbers_list = [1,2,3]
# new_numbers = [n+1 for n in numbers_list]
# print(new_numbers)
#
# name = "Shaun"
# new_list = [letter for letter in name]
# print(new_list)
#
# range_num = range(1,5)
# print(range_num)
# range(1, 5)
# double = [(item*2) for item in range_num]
# print(double)

# range_num = range(1,5)
# range(1, 5)
# square = [(item*item) for item in range_num]
# print(square)

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [(number*number) for number in numbers]
# print(squared_numbers)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = [number for number in numbers if number % 2 == 0]
print(result)
