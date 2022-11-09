# input
coins = int(input("How many cents? (1-100):\n"))

# calculate the cents
fifty_cent = coins // 50
coins -= (fifty_cent * 50)

twenty_cent = coins // 20
coins -= (twenty_cent * 20)

ten_cent = coins // 10
coins -= (ten_cent * 10)

five_cent = coins // 5
coins -= (five_cent * 5)

two_cent = coins // 2
coins -= (two_cent * 2)

# f String:
print(f"Amount of 50 cents: {fifty_cent}\n"
      f"Amount of 20 cents: {twenty_cent}\n"
      f"Amount of 10 cents: {ten_cent}\n"
      f"Amount of 5 cents: {five_cent}\n"
      f"Amount of 2 cents: {two_cent}\n"
      f"Amount of 1 cent: {coins}")
