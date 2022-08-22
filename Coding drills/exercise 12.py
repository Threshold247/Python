#  Write a Python program to print the calendar of a given month and year.
# Note : Use 'calendar' module.

import calendar

mth = int(input("Enter a month: "))
yr = int(input("Enter a yr: "))

mydate = calendar.month(yr, mth)
print(mydate)
