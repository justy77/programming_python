# input length
length = float(input("Give the trip length:\n"))

# consumption with the average 0f 6.5 Liters per 100 km
consumption = (length/100) * 6.5

# print and round the consumption to one decimal
print("Consumption:", round(consumption, 1), "l")
