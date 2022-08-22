# Write a Python program to convert the distance (in feet) to inches, yards, and miles.

def convert():
    x = float(input("Enter a value to convert: "))
    inches = x * 12
    yards = x/3
    miles = x/5280
    print(inches, "inches")
    print(yards, "yards")
    print(round(miles, 3), "miles")


convert()
