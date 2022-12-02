# create variables
cities = ["Rome", "Athens", "Stockholm", "London", "Dublin", "Paris"]
# Sort the list alphabetically
cities.sort()

# row number of each city, starting from 1
for i in range(len(cities)):
    # list index
    print(f"{i + 1}: {cities[i]}")
