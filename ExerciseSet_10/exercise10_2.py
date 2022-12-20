choice = input("Would you like to read or write into guestbook (r/w)?\n")
# if user wants to read
if choice == "r":
    file_handler = open("guestbook.txt", "r")
    content = file_handler.read()
    file_handler.close()
    print(content)
# if user wants to write
elif choice == "w":
    file_handler = open("guestbook.txt", "a")
    content = input("Write a new message:\n")
    content = content + "\n"
    file_handler.writelines(content)
    file_handler.close()
