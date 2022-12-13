from colorama import Fore, Style
from datetime import date

years = []
#  birth years of five different people
for i in range(5):
    year = int(input(f"Give the birth year of person {i + 1}:\n"))
    years.append(year)

current_year = date.today()
print("\nLet's process all birth years ...")
for i in range(len(years)):
    # Each given age has to be between 0 and 125
    # If the age is within the accepted limits, print ”age OK!” in green text.
    if 0 <= (current_year.year - years[i]) <= 125:
        print(Fore.GREEN + f"{current_year.year - years[i]} years old, age OK!")
    else:
        # If the age is not within the accepted limits, print "incorrect age." in red text
        print(Fore.RED + f"{current_year.year - years[i]} years old, incorrect age.")
# After all birth years have been processed, print the text "All done!" in normal text
print(Style.RESET_ALL + "All done!")
