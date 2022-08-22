#  Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged.

test = input("Enter a sentence: ")

if test.startswith("Is") or test.startswith("is"):
    print(test)
else:
    print("Is", test)
