# input
number1 = int(input("Give first number:\n"))
number2 = int(input("Give second number:\n"))

# test if second number is bigger than the first
if number1 < number2:
    print(f"Bigger number = {number2}")
# test if first number is bigger than the second
elif number2 < number1:
    print(f"Bigger number = {number1}")
# if the numbers are equal
else:
    print("Numbers are equal.")