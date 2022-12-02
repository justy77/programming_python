while True:
    multi = int(input("Which multiplication table do you want to see? (1-10). 0 stops program.\n"))

    # 0 stops program
    if multi == 0:
        print("0 stops program!")
        break

    else:
        try:
            #  check that the number given by the user is between 0 and 10
            if 0 < multi <= 10:
                # multiplication table in the range of 1-10
                for i in range(10):
                    # puts second number 1 higher
                    i += 1
                    # calculation
                    print(f"{multi} x {i} = {multi * i}")
            else:
                # number not in format 1-10
                print("Wrong number format.\n")
                pass
        except:
            print("Stop application?")
