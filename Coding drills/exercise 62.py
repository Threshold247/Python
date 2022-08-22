# Write a Python program to convert all units of time into seconds

def conversion():
    days = int(input("Enter days: "))
    hour = int(input("Enter hours: "))
    minutes = int(input("Enter minutes: "))
    seconds = (days*24*3600)+(hour*60*60) + (minutes*60)
    print(seconds)


conversion()
