# input legs
first_leg = float(input("Give the first leg:\n"))
second_leg = float(input("Give the second leg:\n"))

# hypotenuse c = root a² + b²
hypotenuse = (first_leg ** 2) + (second_leg ** 2)
# 0.5 to remove Root and round into 2 decimals
hypotenuse = round(hypotenuse ** 0.5, 2)

# f String
print(f"Hypotenuse: {hypotenuse} m")
