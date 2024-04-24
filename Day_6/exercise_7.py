filenames = ["a.txt", "b.txt", "c.txt"]
for filename in filenames:
    file = open(filename, "r")
    text = file.read()
    file.close()
    print(text)
    