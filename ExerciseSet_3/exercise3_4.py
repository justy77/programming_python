# input
money = int(input("Give money:\n"))
cost = int(input("Purchase cost:\n"))

# if the costs are higher than the money, you have to give more money:
if cost - money > 0:
    money = money + int(input("Not enough money, give more:\n"))

# if the costs are higher than the money, and you don't have more money:
if cost - money > 0:
    print("You don't have enough money.")

# if the costs are same like money or lower:
if cost - money <= 0:
    print(f"Thank you. Here's the change:{money - cost}€")
