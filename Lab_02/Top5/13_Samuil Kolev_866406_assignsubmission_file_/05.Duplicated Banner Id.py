import time
start_time = time.time()

idTxt = open("lucky_ids4.txt").read()

idList = idTxt.split('\n')

duplicatedValues = []
testList = []

for i in idList:
    if i in testList:
        duplicatedValues.append(i)

    testList.append(i)

print(' '.join(duplicatedValues))

end_time = time.time()

print("\nRunning time: ", end_time-start_time)