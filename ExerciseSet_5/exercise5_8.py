# Create an application that asks the user for a word. After this, ask
# the user for a shift number. Based on the word and the shift
# number, transform the word according to Caesar's cipher, and print
# the result.

message = input("Give a phrase:\n").lower()
shift_number = int(input("Give a shift number:\n"))

# alphabetic:
letters = "abcdefghijklmnopqrstuvwxyz"

# create mapping
mapping = letters[shift_number:] + letters[:shift_number]

# translate
give = str.maketrans(letters, mapping)

# string for translation
ciphered = message.translate(give)

print(ciphered)
