# input
salary = float(input("Your monthly salary:\n"))
tax_percentage = float(input("Your tax percentage:\n"))

# taxes including the percentage from salary and round to two decimals
taxes = salary * (tax_percentage * 0.01)
earnings = salary - taxes
earnings = round(earnings, 2)
taxes = round(taxes, 2)

# f String
print(f"Earnings: {earnings} €\n"
      f"Taxes: {taxes} €")
