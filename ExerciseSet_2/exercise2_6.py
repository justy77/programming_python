import math

# fruit salad calculation !2 or 3 bananas = /3 or /2!
cherry = (2 + 2 * 2 + 2 - 2 - 2) / 2
apple = (math.sqrt(3 + 10 - 4) / 3) + ((5 ** 3) - 5) / 20 + 3
banana = (cherry + 10) / 3
orange = apple - 9
pear = (banana * 3) - 8


# result calculation
result = apple - (banana * 2) + (pear + cherry) * orange

# f String
print(int(result))
