#  Write a Python program to get an absolute file path.

from pathlib import Path
p = Path("mbox-short.txt").resolve()
print(p)
