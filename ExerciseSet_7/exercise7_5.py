import json
import urllib.request

url = "https://edu.frostbit.fi/api/weather/"
req = urllib.request.Request(url)
raw_data = urllib.request.urlopen(req).read().decode("UTF-8")
weather = json.loads(raw_data)

strongest_wind = [0, 0]
weakest_wind = [999, 999]

# area lapland
sum_lapland = 0
num_lapland = 0

# area middle
sum_middle = 0
num_middle = 0

# area south
sum_south = 0
num_south = 0

# max & min wind
for i in weather:
    if i["wind"] > strongest_wind[0]:
        strongest_wind.clear()
        strongest_wind.insert(0, i["wind"])
        strongest_wind.insert(1, i["location"])
    else:
        if i["wind"] < weakest_wind[0]:
            weakest_wind.clear()
            weakest_wind.insert(0, i["wind"])
            weakest_wind.insert(1, i["location"])

# areas average wind
for city in weather:
    wind = city['wind']
    location = city['location']
    if city['area'] == 'lapland':
        sum_lapland = sum_lapland + city['wind']
        num_lapland += 1
    if city['area'] == 'middle':
        sum_middle = sum_middle + city['wind']
        num_middle += 1
    if city['area'] == 'south':
        sum_south = sum_south + city['wind']
        num_south += 1

# f print
print(f"Strongest wind today at location: {strongest_wind[1]}, {strongest_wind[0]} m/s")
print(f"Weakest wind today at location: {weakest_wind[1]}, {weakest_wind[0]} m/s")

print(f"\nAverage wind, Lapland: {round((sum_lapland / num_lapland), 1)} m/s")
print(f"Average wind, Middle part of Finland: {round((sum_middle / num_middle), 1)} m/s")
print(f"Average wind, Southern Finland: {round((sum_south / num_middle), 1)} /s")
