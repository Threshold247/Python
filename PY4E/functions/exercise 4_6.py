# storing function
def computepay(h, r):
    if hours > 40:
        normalPay = hours*rate
        extraHours = hours-40
        extraRate = rate*0.5
        overtime = extraRate*extraHours
        totalPay = normalPay+overtime
    else:
        totalPay = hours*rate
    return totalPay


hours = float(input("Enter hours: "))
rate = float(input("Enter rate: "))

p = computepay(hours, rate)  # call function with arguments
print("Pay", p)
