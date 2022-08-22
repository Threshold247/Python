# Write a Python program to get the current username

import getpass
import os

print(os.environ['USERNAME'])
# OR
print(getpass.getuser())
