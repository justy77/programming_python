# list of dictionaries:
shop_cart = [
    {"name": "Beehive - lamp", "price": 999.9},
    {"name": "Malm - bed", "price": 169.9},
    {"name": "Moomin - mug set", "price": 59.9},
    {"name": "Nemo - divan", "price": 699.9},
    {"name": "Ritz - armchair", "price": 369.9}
]

# Calculate the sum:
sum_total = 0
print("Receipt:")
for i in shop_cart:
    print(f" - {i['name']}")
    sum_total = sum_total + i['price']

# Calculate the amount of VAT as well 24%:
vat = sum_total * 0.24
print()
print(f"Total sum: {sum_total} €.")
print(f"VAT of the total purchase: {vat} €.")
print("Please come again!")
