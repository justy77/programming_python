# contains a list called inventory, which
# consists of other lists (fruits, berries and vegetables)
fruits = ["apple", "pear", "banana"]
berries = ["strawberry", "blueberry", "blackberry"]
vegetables = ["carrot", "kale", "cucumber"]
collection = [fruits, berries, vegetables]

# Print the contents of the inventory list by using a loop, that has another
# loop inside it:
for i in collection:
    for x in i:
        print(x)
