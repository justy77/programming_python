# input
outside_urban = float(input("Kilometers outside urban area:\n"))
inside_urban = float(input("Kilometers within urban area:\n"))

# consumption with outside_urban = 5.1 Liters/100 KM and inside_urban = 7.5 Liters/100 KM
consumption = (outside_urban / 100) * 5.1 + (inside_urban / 100) * 7.5

# consumption with outside_urban = 6.12 Liters/100 KM and inside_urban = 3.75 Liters/100 KM
consumption2 = (outside_urban / 100) * 6.12 + (inside_urban / 100) * 3.75

# f String
print(f"Consumption: {consumption} l")
print(f"Consumption 2: {consumption2} l")
