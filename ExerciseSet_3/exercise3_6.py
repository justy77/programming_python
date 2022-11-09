# input:
year = int(input("Give year:\n"))
leap_year = False

# If the year is divisible by 100, it's not a leap year
# If the year is divisible by 4, it's a leap year
# In other cases, it's not a leap year
# If the year is divisible by 400, it's always a leap year.
if year % 4 == 0:
    if year % 100 != 0 or year % 400 == 0:
        leap_year = True
else:
    leap_year = False

if leap_year:
    print("Leap year: YES")

else:
    print("Leap year: NO")
