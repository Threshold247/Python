#  Write a Python program to check whether a file exists

import os.path

print(os.path.isfile("main.py"))
# OR
print(os.path.exists("main.py"))
print(os.path.exists("mbox.txt"))
