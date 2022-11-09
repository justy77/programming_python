# text from moodle:
text = "The quick brown fox jumps over the lazy dog. That \
sentence contains every letter in the English alphabet. Neat!"
print(text)

# replace fox with duck:
print(text.replace("fox", "duck"))

# If the word cannot be found in the text-variable, print "Word not found.".
# If the word was found in the text-variable, remove the word from the
# text-variable, and print the new version of the text-variable on the screen
word_remove = str(input("Which word do you want to remove?\n"))
new = text.replace(word_remove, " ")
print(new)

# Print the number of characters in the text-variable
print(str(len(new)) + " characters")

# Replace the dots/periods in the text-variable into newlines.
print(new.replace(".", "\n"))

# input usertext:
usertext = str(input("Write a new sentence:\n"))
u_text = usertext[0:]

if u_text == usertext[0:20]:
    print(u_text)

elif u_text == usertext[20:30]:
    usertext += "..."
    print(u_text)
