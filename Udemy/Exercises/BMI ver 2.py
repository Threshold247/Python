# 🚨 Don't change the code below 👇


height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

bmi = weight/height**2
print(bmi)
conv_bmi = round(bmi)
print(conv_bmi)


if conv_bmi <= 18.5:
    print(f"Your BMI is {conv_bmi}, you are underweight.")
elif conv_bmi <= 25:
    print(f"Your BMI is {conv_bmi}, you have a normal weight.")
elif conv_bmi <= 30:
    print(f"Your BMI is {conv_bmi}, you are slightly overweight.")
elif conv_bmi <= 35:
    print(f"Your BMI is {conv_bmi}, you are obese.")
else:
    print(f"Your BMI is {conv_bmi}, you are clinically obese.")
