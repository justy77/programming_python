from functions import *

# Ask the user to provide the list of participants in one line, all
# names separated by a comma
names = input("Write all participants, separated by a comma:\n")
list_of_names = names.split(",")
print()

# show_numbered_list(title, data) that takes two
# parameters: the title text and a list of participant names
show_numbered_list("Original order:", list_of_names)
list_of_names.sort()
show_numbered_list("Alphabetic order by first name:", list_of_names)
list_of_names = [" ".join(reversed(p.split(" "))) for p in list_of_names]
list_of_names.sort()
show_numbered_list("Alphabetic order by last name:", list_of_names)
