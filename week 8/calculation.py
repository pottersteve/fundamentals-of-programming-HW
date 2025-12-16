from math import pi

print("Enter a float number for the radius:")
radius = float(input())

cir_result = round(2 * pi * radius, 3)
area_result = round(pi * radius ** 2, 3)

print(f"The circumference is: {cir_result}")
print(f"The area is: {area_result}")