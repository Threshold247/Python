def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return("Leap year.")
            else:
                return("Not leap year.")
        else:
            return("Leap year.")
    else:
        return("Not leap year.")


def days_in_month(y, m):
    """Checks the days in a given month and year."""
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(y) == "Leap year." and m == 2:
        return 29
    else:
        return month_days[m-1]


# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(y=year, m=month)
print(days)
