from colorama import Back

# numbers between 2 - 100
for numbers in range(2, 101):
    for i in range(2, numbers):
        # if number can divide by itself, print red and break
        if (numbers % i) == 0:
            # f for concatenate str error
            print(Back.RED + f"{numbers}")
            break
    else:
        # f for concatenate str error for the prime numbers
        print(Back.GREEN + f"{numbers}")
