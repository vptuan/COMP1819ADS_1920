id = "001062275"
found = False
with open("lucky_ids.txt", "r") as file:
    for line in file.readlines():
        line = line.rstrip()
        if id == line:
            found = True

print("Yes" if found else "No")