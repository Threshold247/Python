# Write a Python program to accept a filename from the user and print the extension of that


filename = input("Enter filename: with ext: ")
newfile = filename.split(".")
print(newfile[1])
