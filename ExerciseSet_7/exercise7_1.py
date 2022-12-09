# Create the following dictionary
cafe = {
    "name": "Imaginary Cafe Ltd.",
    "website": "https://edu.frostbit.fi/sites/cafe/en",
    "categories": [
        "cafe",
        "tea",
        "lunch",
        "breakfast"
    ],
    "location": {
        "city": "Rovaniemi",
        "address": "Test address 22",
        "zip_code": "FI-96100"
    }
}

# print contents of the dictionary
print(cafe["name"])
print(cafe["location"]["address"])
print(cafe["location"]["zip_code"], cafe["location"]["city"])
print("\n")
print(cafe["website"])

separator = ", "
text = "Services: "
new_text = ""
for i in cafe["categories"]:
    new_text = separator.join(cafe["categories"])
text += new_text

print(text)
