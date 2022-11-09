import math

# input quadratic equation ( a,b,c )
a = float(input("Give first value:\n"))
b = float(input("Give second value:\n"))
c = float(input("Give third value:\n"))

# calculation quadratic equation:
x1 = ((b * (- 1)) + math.sqrt((b ** 2) - 4 * a * c)) / (2 * a)
x2 = ((b * (- 1)) - math.sqrt((b ** 2) - 4 * a * c)) / (2 * a)

# x provides two different values
# f String
print(f"x1 = {x1} and x2 = {x2}")

