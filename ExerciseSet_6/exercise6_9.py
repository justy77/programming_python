price = int(input("What is the original price of the car?:\n"))
year = int(input("What is the year of manufacturing??:\n"))
km = int(input("What is the mileage?:\n"))
category = int(input("What is the category?:\n"))
car_import = str(input("Is it an imported car?: (y/n)\n"))

if category == 2:
    if km >= 30000:
        price = price / 100.0 + 1

