# input
temperature = int(input("Which temperature: \n"))
humidity = int(input("Which humidity: \n"))

# boolean variables:
freezing = False
heatwave = False
raining = False
hailstorm = False

# If the given temperature is less than 0, set the freezing-variable to True
if temperature < 0:
    freezing = True

# If the humidity is over 80, set the raining-variable to True
if humidity > 80:
    raining = True

# if the temperature is lower than -20 degrees, set the hailstorm-variable to True instead of the raining-variable
if temperature <= -20:
    raining = False
    hailstorm = True

# If the temperature is over 20 degrees, set the heatwave-variable to True.
if temperature >= 20:
    heatwave = True

#  If the freezing-variable is True, print "It's freezing outside."
if freezing:
    print("It´s freezing outside.")

# If the raining-variable is true, print "It's raining."
if raining:
    print("It´s raining.")

#  If the hailstorm-variable is True, print "There's a hailstorm, be careful!"
if hailstorm:
    print("There´s a hailstorm, be careful!")

# If the heatwave-variable is true, print "Heatwave! Remember to hydrate!"
if heatwave:
    print("Heatwave! Remember to hydrate!")

# If it's raining and there's a heatwave at the same time, print also "It's damp and hot."
if heatwave and raining:
    print("It´s damp and hot.")


