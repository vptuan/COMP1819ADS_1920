# without min max functions
"""import sys

n = int(input())

minNum = sys.maxsize
maxNum = -sys.maxsize

for i in range(n):
    num = int(input())

    if num < minNum:
        minNum = num

    if num > maxNum:
        maxNum = num

tup = minNum, maxNum
print(tup)"""

# with min max functions
n = int(input())

arr = []

for i in range(n):
    num = int(input())
    arr.append(num)

tup = min(arr), max(arr)
print(tup)
