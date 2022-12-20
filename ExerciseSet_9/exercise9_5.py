from functions import *

while True:
    # 1 = box, 2 = ball and 3 = pipe, 0 = stop the application
    choice = input("Select the operation (1-3), 0 stops the application:\n")
    if choice == "1":
        width = float(input("Give box width:\n"))
        height = float(input("Give box height:\n"))
        depth = float(input("Give box depth:\n"))
        volume = box_volume(width, height, depth)
        print(f"Box volume: {volume} m3\n")
    elif choice == "2":
        radius = float(input("Give ball radius:\n"))
        volume = ball_volume(radius)
        print(f"Ball volume: {volume} m3\n")
    elif choice == "3":
        radius = float(input("Give pipe radius:\n"))
        length = float(input("Give pipe length:\n"))
        volume = pipe_volume(radius, length)
        print(f"Pipe volume: {volume} m3\n")
    elif choice == "0":
        print("Thank you for using our application!")
        break
