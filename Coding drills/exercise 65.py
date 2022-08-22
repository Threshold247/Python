#  Write a Python program to convert seconds to day, hour, minutes and seconds

def convert_seconds():
    secs = float(input("Enter seconds: "))
    hours = secs/60/60
    days = secs/60/60/24
    minutes = secs/60

    print("Days: ", days)
    print("Hours: ", round(hours, 4))
    print("Minutes: ", minutes)


convert_seconds()
