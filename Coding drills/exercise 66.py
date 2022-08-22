# Write a Python program to calculate body mass index

def body_mass():
    kg = float(input("Enter weight in kgs: "))
    height = float(input("Enter height in meters: "))
    BMI = kg/(height**2)
    BMI = round(BMI, 2)

    if BMI <= 18.5:
        print("BMI: ", BMI, "You are underweight")
    elif BMI > 18.5 and BMI <= 25:
        print("BMI: ", BMI, "Your weight is normal")
    else:
        print("BMI: ", BMI, "You are overweight")


body_mass()
