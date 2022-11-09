import random

# choose random value between 1 - 10
value = random.randint(1, 10)

# choose random value between 2 - 10
first_side = random.randint(2, 10)
second_side = random.randint(2, 10)

# calculation of the area of the rectangle (a * b)
area = first_side * second_side

# f String
print(f"Random number: {value}\n"
      f"First random side: {first_side}\n"
      f"Second random side: {second_side}\n"
      f"Rectangle area: {area}")
