try:
    # create variable:
    biggest = 0
    # input of 5 numbers:
    for i in range(5):
        number = int(input("Give a number:\n"))
        value = int(number)
        # check if the number is negative:
        if value < 0:
            print("Input must be a positive integer")
        # if the number is not negative, search the biggest:
        if number > 0:
            if number > biggest:
                biggest = number
        else:
            pass
    # Print only the biggest number:
    print(f"The biggest number from user: {biggest}")

except:
    print("Not a number!")
