# use date module:
from datetime import date

# get current date:
today = str(date.today())
day = today[-2:]
month = today[5:7]
year = today[0:4]
client_name = "John Doe"
year_of_birth = 1984
balance = 345

# f print:
all_variables = f"{client_name} ({year_of_birth}), balance: {balance} €, updated on {day}.{month}.{year}."

print(all_variables)

