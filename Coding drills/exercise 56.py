# Write a Python program to get height and width of the console window.

import os
ts = os.get_terminal_size()
print(ts.lines)
print(ts.columns)
