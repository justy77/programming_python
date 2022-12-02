from math import pi

while True:
    try:
        # ask the user for the radius of a circle
        radius = int(input("Give radius:\n"))
        # calculates the area of the circle and prints rounded result
        circle_area = pi * (radius ** 2)
        circle_area = round(circle_area, 2)
        print(circle_area)

        # ask the user whether they want to continue using the program or not (y/n)
        keep_going = input("Do you want to continue? (y/n)\n")
        # if n, stop the application.
        if keep_going == "n":
            break
        else:
            pass

    except:
        pass
