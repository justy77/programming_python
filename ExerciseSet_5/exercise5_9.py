# List of  10 names of different persons
names = ["Daniel", "Maria", "Sabine", "Uwe", "Liam", "Marinella", "Thomas", "Senta", "Poc", "Chris"]

for i in names:
    # Names that do not contain the letter s
    if "s" not in i:
        print("Name without s:")
        print(i)

    # Names that do not contain the letter e
    if "e" not in i:
        print("Name without e:")
        print(i)

    # Names that are less than 8 characters long
    if len(i) <= 8:
        print("Name less than 8 characters:")
        print(i)


# Names with maximum vowels:
def vowels(s):
    # a e i o u = vowels
    vowel_list = s.count("a") + s.count("e") + s.count("i") + s.count("o") + s.count("u")
    return vowel_list


# create empty string and search in names
result = []
for x in names:
    result.append(vowels(x))
x = result.index(max(result))
vowel = names[x]

print("Word with most vowels : " + str(vowel))
