# input
price = float(input("Give the price without VAT:\n"))

# increase the price by 24% => multiply by 1.24
price = price * 1.24

# print and round the price to two decimal
print("Price with VAT: ", round(price, 2), "€")
