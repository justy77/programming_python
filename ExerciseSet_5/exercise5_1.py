# create variables
number = 0
sum_up = 0

# application that prints the numbers 1-50 on separate lines with "while"-statement
print("Application with while - statement:")
while number <= 49:
    number += 1
    print(number)

# application that prints the numbers 1-50 on separate lines with "for"-statement
print("\nApplication with for - statement:")
for numb in range(50):
    print(numb)

# sums up all numbers in the range of 1-30
for numb in range(30):
    sum_up += numb + 1
# f print
print(f"Sum: {sum_up}")

# all years between 2005 and 2010 on the same line
# first I wanted to use an "if-statement" by habit..
print_years = ""
first_year = 2005

while first_year <= 2010:
    print_years += str(first_year) + " "
    first_year += 1

print(print_years)
