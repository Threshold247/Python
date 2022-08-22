# Write a Python program to filter a dictionary based on values.
# Original Dictionary:
# {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
# Marks greater than 170:
# {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}

data = {'Cierra Vega': 175, 'Alden Cantrell': 180,
        'Kierra Gentry': 165, 'Pierre Cox': 190}
newData = {}

for key, value in data.items():
    if value > 170:
        newData[key] = value
print(f"New Marks: {newData}")

# OR
print("New Marks:", {key: value for(key, value)
      in data.items() if value > 170})
