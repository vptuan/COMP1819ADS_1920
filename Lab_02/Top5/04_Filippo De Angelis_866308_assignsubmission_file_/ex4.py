# Filippo De Angelis
import time

ids = []

with open("lucky_ids2.txt", "r") as file:
    for line in file.readlines():
        line = line.rstrip()
        ids.append(int(line))


max1 = max2 = max3 = ids[0]
for id in ids:
    if id > max1:
        max3 = max2
        max2 = max1
        max1 = id
    elif id > max2:
        max3 = max2
        max2 = id
    elif id > max3:
        max3 = id

start_time = time.time()
print("00{} 00{} 00{}".format(max1, max2, max3))
end_time = time.time()
print("\nRunning time: ", end_time-start_time)