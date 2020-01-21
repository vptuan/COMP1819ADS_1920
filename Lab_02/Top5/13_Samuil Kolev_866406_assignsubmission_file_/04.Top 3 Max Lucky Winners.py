import time

start_time = time.time()

idTxt = open("lucky_ids2.txt").read()

idList = idTxt.split('\n')

copyIdList = idList.copy()

topThree = []

for i in range(3):
    topThree.append(max(copyIdList))
    copyIdList.remove(max(copyIdList))

print(' '.join(topThree))

"""idTxt = open("lucky_ids.txt").read()

idList = idTxt.split('\n')

maxNumOne = max(idList)

topThree = [maxNumOne]

maxNumTwo = min(idList)

for bannerId in idList:
    if maxNumTwo < bannerId < maxNumOne:
        maxNumTwo = bannerId

topThree.append(maxNumTwo)

maxNumThree = min(idList)

for bannerId in idList:
    if maxNumThree < bannerId < maxNumTwo:
        maxNumThree = bannerId

topThree.append(maxNumThree)

print(' '.join(topThree))"""

end_time = time.time()

print("\nRunning time: ", end_time-start_time)