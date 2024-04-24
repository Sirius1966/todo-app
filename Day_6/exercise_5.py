mew_member = input("Enter a new Member: ")
file = open("members.txt", "a")
file.write(mew_member)
file.close()
