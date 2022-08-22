# Write a Python program to list all files in a directory in Python

from os import listdir
from os.path import isfile, join

files_list = [f for f in listdir('Downloads') if isfile(join('Downloads', f))]
print(files_list)
