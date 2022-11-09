# input:
text = str(input("Give some text:\n"))

# reverse the text
text_reversed = text[::-1]
print(text_reversed)

# if the original text is identical to the reversed text, it is considered a palindrome
# if the word is a palindrome, print "Palindrome: YES", if not, print "Palindrome: NO".
# if the user inputs an empty string, print "Your text is empty."
if text != "":
    if text_reversed == text:
        print("Palindrome: YES")
    else:
        print("Palindrome: NO")
else:
    print("Your text is empty.")
