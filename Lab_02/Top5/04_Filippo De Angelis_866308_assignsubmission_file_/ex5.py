ids = []
doubles = []

with open("lucky_ids.txt", "r") as file:
    for line in file.readlines():
        line = line.rstrip()
        if line in ids:
            doubles.append(line)
        ids.append(line)

for d in doubles:
    print(d)