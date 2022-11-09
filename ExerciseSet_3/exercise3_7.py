type = str(input("Is it a parcel or a letter?:\n"))
weigth = int(input("What is the weight?:\n"))

costs_letter = 0.5
costs_parcel = 2.0

if type.lower() == "letter":
    # costs for a letter
    if weigth < 200:
        print(f"Cost: {costs_letter}€\n")
    elif 200 < weigth < 501:
        costs = weigth // 100
        extra_costs = costs * 0.04
        print(f"Cost: {costs_letter + extra_costs}€")

    # first ask if fits:
    mailbox = input("Does the letter fits in the mailbox? (y/n)\n")
    costs = weigth // 100
    extra_costs = costs * 0.07

    #  if letter doesn´t fit in the mailbox there is 2.0 additional costs
    if mailbox.lower() == "n":
        extra_costs = extra_costs + 2.0
    print(f"Cost: {costs_letter + extra_costs}€")

if type.lower() == "parcel":
    if weigth < 200:
        print(f"Cost: {costs_parcel}€")
    elif 200 < weigth < 501:
        costs = weigth // 100
        extra_costs = costs * 0.08
        print(f"Cost: {costs_parcel + extra_costs}€")

    else:
        costs = weigth // 100
        extra_costs = costs * 0.18
        print(f"Cost: {costs_parcel + extra_costs}€")
