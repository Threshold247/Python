# Write a Python program to get file creation and modification date/times

import os.path
import time

print("Last modified: %s" % time.ctime(os.path.getmtime("mbox-short.txt")))
print("Created: %s" % time.ctime(os.path.getctime("mbox-short.txt")))
