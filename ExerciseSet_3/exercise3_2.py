# input:
temperature = int(input("Give the temperature:\n"))

# temperature between 0-10:
if -1 < temperature < 11:
    print("COLD")
# temperature between 11-15:
elif 10 < temperature < 16:
    print("CHILLY")
# temperature between 16-20:
elif 15 < temperature < 21:
    print("NORMAL TEMPERATURE")
# temperature between 21-25:
elif 20 < temperature < 26:
    print("WARM")
# temperature between 26-30:
elif 25 < temperature < 31:
    print("HOT")
