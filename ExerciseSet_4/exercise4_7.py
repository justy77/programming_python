# input
number = input("Give numbers:\n")

# variables
word = ""
new_word = ""
numb = ""
new_numb = ""

# unpack method
unpack = [*number]
unpack2 = number.split()

# allow only values of maximum of 5 different numbers
if len(number) <= 5:
    for x in unpack:
        # declare numbers and words
        if x == "0":
            word = "zero"
        elif x == "1":
            word = "one"
        elif x == "2":
            word = "two"
        elif x == "3":
            word = "three"
        elif x == "4":
            word = "four"
        elif x == "5":
            word = "five"
        elif x == "6":
            word = "six"
        elif x == "7":
            word = "seven"
        elif x == "8":
            word = "eight"
        elif x == "9":
            word = "nine"
        # add space between the new words
        new_word = new_word + word + " "
else:
    print("Not more than 5 numbers!")

print(new_word)

# the other way around
if len(number):
    for x in unpack2:
        # declare numbers and words
        if x == "zero":
            numb = "0"
        elif x == "one":
            numb = "1"
        elif x == "two":
            numb = "2"
        elif x == "three":
            numb = "3"
        elif x == "four":
            numb = "4"
        elif x == "five":
            numb = "5"
        elif x == "six":
            numb = "6"
        elif x == "seven":
            numb = "7"
        elif x == "eight":
            numb = "8"
        elif x == "nine":
            numb = "9"
        # add space between the new words
        new_numb = new_numb + numb + " "

print(new_numb)
