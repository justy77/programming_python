from functions import *

amount = float(input("Give amount of your money:\n"))
currency = input("Give currency of your money:\n")
target = input("Give currency to which money should be converted:\n")

converted = convert_money(amount, currency, target)
if amount == 1 and converted == 1:
    print(f"{amount} {currency} = {round(converted, 2)} {target}")
elif amount != 1 and converted == 1:
    print(f"{amount} {currency}s = {round(converted, 2)} {target}")
elif amount == 1 and converted != 1:
    print(f"{amount} {currency} = {round(converted, 2)} {target}s")
elif amount != 1 and converted != 1:
    print(f"{amount} {currency}s = {round(converted, 2)} {target}s")
    