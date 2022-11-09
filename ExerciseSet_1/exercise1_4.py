# input for minute
minute = int(input("Give minutes:\n"))

# division without decimals
hour = minute // 60

# minutes after dividing
minute = minute % 60

# f String:
print(f"{hour}h {minute}min")
