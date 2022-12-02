# create variables
rain = []
average = 0.0

# ask the user 12 times the rain amount of the month
for x in range(12):
    amount_of_rain = float(input("Give rain amount of month:\n"))
    rain.append(amount_of_rain)

# Based on the 12 values, calculate and print the average rain amount rounded to one decimal.
for x in range(len(rain)):
    average += rain[x]
# average = total rain amount / amount of months
average = average / len(rain)

# f print
print(f"Year average for rain = {round(average,1)} mm")
