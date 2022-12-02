# create list
months = ("January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December")

# collections start at 0, but user might
# want to user the actual numbers, therefore - 1
# for example, if user gives 3, we transform it to 2,
# which is then, March
choice = int(input("Give the number of month:\n"))

# print out the required month
print(months[choice - 1])
