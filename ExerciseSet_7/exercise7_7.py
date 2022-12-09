import json
import urllib.request
from list_in_list import Counter
url = "https://liukastumisvaroitus-api.beze.io/api/v1/warnings"
req = urllib.request.Request(url)
raw_data = urllib.request.urlopen(req).read().decode("UTF-8")
data = json.loads(raw_data)

# empty arrays:
first_list = []
second_list = []

# city with the highest/most warning
for warning in data:
    if warning['city'] not in first_list:
        first_list.append(warning['city'])
    second_list.append(warning['city'])

# count the cities:
count_cities = dict(Counter(second_list))

max_city = max(count_cities, key=count_cities.get)

# f print
print(f"{max_city} the most warnings of slippery weather conditions\n")

warning_amount = 0
# f print
print(f"5 latest slippery weather warnings in {max_city}:")

# latest warnings:
for warning in list(reversed(list(data))):
    if warning['city'] == max_city:
        print(f"- {warning['city']}: {warning['created_at']}")
        warning_amount += 1
    if warning_amount == 5:
        break
