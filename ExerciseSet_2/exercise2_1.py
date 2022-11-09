# input sides for box:
import math

first_side = float(input("Give the first side:\n"))
second_side = float(input("Give the second side:\n"))
third_side = float(input("Give the third side:\n"))

# volume of the box:
volume = round(first_side * second_side * third_side, 2)

# f String volume:
print(f"Box volume: {volume} m³")

# input radius for sphere:
radius = float(input("Give the sphere radius:\n"))

# sphere volume (³)
sphere = round((4/3) * math.pi * (radius ** 3), 2)

# f String sphere:
print(f"Sphere volume: {sphere} m³")
