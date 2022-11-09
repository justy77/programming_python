# create values
student = False
number_month = False
special_price = False

# input
study = input("Are you a student? (y/n)\n").lower()

# student or not?
if study == "y":
    student = True
else:
    student = False

# ask the number of the month, when the user is planning to travel.
travel_month = int(input("Travel month? (1-12)\n"))

# The user is entitled to a special price, if they are a student (y) and the reservation is not on months 6 - 8.
if 6 <= travel_month <= 8:
    number_month = False
else:
    number_month = True

if student and number_month:
    special_price = True
    print("Special price!")
else:
    special_price = False
    print("Normal price.")
