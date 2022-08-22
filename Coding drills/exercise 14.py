# Write a Python program to calculate number of days between two dates.
# Sample dates : (2014, 7, 2), (2014, 7, 11)
# Expected output : 9 days


from datetime import date

fdate = date(2022, 7, 12)
sdate = date(2022, 7, 7)

calc = fdate - sdate

print(calc.days, "days")
