score = input("Enter a number between 0.0 and 1.0: ")

try:
    floatScore = float(score)
    if floatScore > 1.0:
        print("Number out of range")
    elif floatScore >= 0.9:
        print("A")
    elif floatScore >= 0.8:
        print("B")
    elif floatScore >= 0.7:
        print("C")
    elif floatScore >= 0.6:
        print("D")
    else:
        print("F")

except:
    print('Not a number')
    quit()
