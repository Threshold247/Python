x = input('Please enter hours: ')
y = input('Please enter rate: ')
try:
    hours = float(x)
    rate = float(y)
except:
    print("Enter a number")
    quit()  # stops program from continuing

if hours > 40:
    normalPay = hours*rate
    extraHours = hours-40
    extraRate = rate*0.5
    overtime = extraRate*extraHours
    totalPay = normalPay+overtime
else:
    totalPay = hours*rate
    #print("Normal", totalPay)
print("Pay: ", totalPay)
