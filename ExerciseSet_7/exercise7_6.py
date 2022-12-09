# collection of multiple restaurants
restaurants = [
    {
        "name": "North Delish",
        "rating": 4.5,
        "reservations": True,
        "services": [
            "lunch",
            "dinner"
        ],
        "price_level": 5,
        "location": "Rovaniemi"
    },
    {
        "name": "Food Galore",
        "rating": 3.8,
        "reservations": False,
        "services": [
            "breakfast",
            "lunch"
        ],
        "price_level": 3,
        "location": "London"
    },
    {
        "name": "Snacksy Ltd",
        "rating": 3.2,
        "reservations": False,
        "services": [
            "lunch",
            "dinner",
            "night"
        ],
        "price_level": 2,
        "location": "Berlin"
    },
    {
        "name": "Mc Donald's",
        "rating": 2.7,
        "reservations": True,
        "services": [
            "breakfast",
            "lunch",
            "dinner",
            "night"
        ],
        "price_level": 2,
        "location": "Los Angeles"
    },
    {
        "name": "Pizza Hut",
        "rating": 4.7,
        "reservations": True,
        "services": [
            "lunch",
            "dinner",
            "night"
        ],
        "price_level": 4,
        "location": "Toronto"
    }
]

# Finally, ask the user a series of questions of the type of restaurant the user is looking for
rating = int(input("Which star rating at least for the restaurant? (1-5)\n"))
price = int(input("What is the maximum price level you're looking for? (1-5)\n"))
reservation = input("Would you like to make a reservation before hand? (y/n)\n")
time = int(input("In what time would you like to arrive? (0 – 23)\n"))

# value:
match = 0

# request time:
if 0 <= time <= 5:
    time = "night"
elif 6 <= time <= 10:
    time = "breakfast"
elif 11 <= time <= 16:
    time = "lunch"
elif 17 <= time <= 24:
    time = "dinner"

# ask for reservations:
if reservation == "y":
    reservation_status = True
else:
    reservation_status = False

# loop over different restaurants:
for restaurant in restaurants:
    if (
            restaurant['rating'] >= rating and restaurant['price_level'] <= price
            and restaurant['reservations'] == reservation_status and time in restaurant['services']
    ):
        print(restaurant['name'])
        match += 1

if match == 0:
    print("No matching restaurants found, unfortunately!")
    