# fruit list:
basket = ["apple", "banana", "cherry", "carrot", "potato", "tomato", "cabbage"]

# input:
word = input("Which word to ignore?\n")

# check if word in array:
if word not in basket:
    print("Word not found.")
    if word.isnumeric():
        print("Numeric")
    else:
        print("Not numeric")
else:
    for i in basket:
        if i == word:
            pass
        else:
            print(i)
