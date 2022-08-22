# Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2
# Test Data :
# color_list_1 = set(["White", "Black", "Red"])
# color_list_2 = set(["Red", "Green"])
# Expected Output :
# {'Black', 'White'}

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

print(color_list_1.difference(color_list_2)) #Compare what is in list 1 vs list 2
print(color_list_2.difference(color_list_1)) #Compare what is in list 2 vs list 1
