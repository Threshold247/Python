# Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5

def test(x, y):
    xint = int(x)
    yint = int(y)
    if xint == yint:
        print('True')
    elif xint+yint == 5:
        print('True')
    elif abs(xint-yint) == 5:
        print('True')
    else:
        print('False')


test(1, 1)
test(2, 3)
test(10, 5)
test(5, 10)
test(1, 2)
