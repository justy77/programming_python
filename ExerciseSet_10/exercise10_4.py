import json
file_handler = open("countries.json", "r")
content = file_handler.read()
file_handler.close()

countries = json.loads(content)

print("All countries and capitals:")
for country in countries:
    print(f"{country['country']}: {country['capital']}")

filter_out = input("\nFilter a country/capital with a single letter:\n")

# filter country or capital out with first letter
for country in countries:
    if country['country'][0] == filter_out:
        print(f"{country['country']}: {country['capital']}")
