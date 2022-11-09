try:
    # Ask the user for two different numbers
    first_number = int(input("First number:\n"))
    second_number = int(input("Second number:\n"))

    # If the user tries to divide by zero, print "You can't divide by zero."
    if second_number == 0:
        print("You can't divide by zero.")
    else:
        # divide the first number by the second number
        print(first_number / second_number)
except:
    # If the user inputs text, print "Incorrect format"
    print("Incorrect format.")
