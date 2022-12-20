import random

file = open("wisewords.txt", "r")
lines = file.readlines()
lines = [line.rstrip() for line in lines]
file.close()

rand_num = random.randint(0, len(lines))

print(f"Today's proverb: \n{lines[rand_num]}")
