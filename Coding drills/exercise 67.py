# Write a Python program to convert pressure in kilopascals to pounds per square inch, a millimeter of mercury (mmHg) and atmosphere pressure.

def convert_kPA():
    kPA = float(input("Enter the kilopascals to convert: "))
    pounds = kPA/6.894757
    mmHg = kPA * 7.5006
    atmos = kPA/101
    print("%.2f psi" % (pounds))
    print("%.2f mmHg:" % (mmHg))
    print("%.2f atmsopheric pressure:" % (atmos))


convert_kPA()
# OR
kpa = float(input("Input the pressure in kilopascals > "))
pressure_in_psi = round(kpa * 0.145038, 3)
pressure_in_mmHg = round(kpa * 7.50062, 3)
pressure_in_atmp = round(kpa * 0.0098692382432766, 3)
print(f"{pressure_in_psi} psi \nor {pressure_in_mmHg} mmHg \nor {pressure_in_atmp} atmp")
