# Write a Python program that will accept the base and height of a triangle and compute the area.
# formula  A = (½) bh square units

def triangle_area():
    base = float(input("Enter the base: "))
    height = float(input("Enter the height: "))
    area = 1/2*base*height
    return area

print(triangle_area())
