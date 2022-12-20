from functions import *
ISSN = input("Give an ISSN-serial:\n")

# status check
status = magazine_serial_check(ISSN)
if status:
    print("Valid ISSN.")
else:
    print("Incorrect ISSN.")
