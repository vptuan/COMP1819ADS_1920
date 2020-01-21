idTxt = open("lucky_ids.txt").read()

idList = idTxt.split('\n')

myId = input()

if myId in idList:
    print("Yes")
else:
    print("No")
