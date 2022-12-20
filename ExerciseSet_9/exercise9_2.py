from functions import *
test = input("Give time: (..h ..min ..sec)\n")

# variables
parts = test.split(" ")
numeric_strings = []
time = []

# test split num function for going threw string
for t in parts:
    numeric_filter = filter(str.isdigit, t)
    numeric_string = "".join(numeric_filter)
    numeric_strings.append(numeric_string)

# time in string
for i in numeric_strings:
    time.append(int(i))

#  three parameters:
hours = time[0]
minutes = time[1]
seconds = time[2]

# total amount of seconds based on the given hours, minutes and seconds
print(count_seconds(hours, minutes, seconds), "seconds in total")
