#!/usr/bin/env python3
# Source: https://www.geeksforgeeks.org/bubble-sort/
# Python program for implementation of Bubble Sort
# From original code by Tuan V; original code - no early exit
# GDR - 001081292 - added tracking metrics

from time import time


def printArray(arr):
    for i in range(len(arr)):
        print("[{:n}]: {:n}".format(i, arr[i]))

# will slow things down in absolute terms, but help tracking metrics
def resetCounters(dummy=None):
    global gnReadCount
    global gnWriteCount
    global gnCompareCount
    gnReadCount = 0
    gnWriteCount = 0
    gnCompareCount = 0



def readCell(array, index):
    global gnReadCount
    gnReadCount += 1
    try:
        return array[index]
    except:
        print('read aborted')
        raise



def writeCell(array, index, value):
    global gnWriteCount
    gnWriteCount += 1
    try:
        array[index] = value
    except:
        print('write aborted')
        raise



def compareCell(value1, value2):
    global gnCompareCount
    gnCompareCount += 1
    return (value1 > value2)



def bubbleSort(arr):

    resetCounters()

    tStart = time()

    n = len(arr)

    # Traverse through all array elements 
    for i in range(n):

        # Last i elements are already in place 
        for j in range(0, n-i-1):

            # traverse the array from 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element
            v1 = readCell(arr, j)
            v2 = readCell(arr, j+1)
            if compareCell(v1, v2):
                writeCell(arr, j, v2)
                writeCell(arr, j + 1, v1)

    print('Execution time (s) : {:f}'.format(time() - tStart))
    print('{:n} pass(es)'.format(i+1))

    return arr



if __name__ == '__main__':

# Driver code to test above 
#unsorted = [64, 34, 25, 12, 22, 11, 90] 
#printArray(unsorted)
    for s in ('random', 'sorted', 'reverse'):
        for n in (100, 1000, 10000):
            data = '{:s}-strings-{:s}.txt'.format(s, str(n))
            print(data)
            with open(data, 'r') as f:
                sorted = bubbleSort([l.rstrip('\n') for l in f])

#print ("Sorted array is:")
#printArray(sorted)

                print('Total elements     : {:n}\nTotal reads        : {:n}\nTotal writes       : {:n}\nTotal compares     : {:n}\n\n'.format(len(sorted), gnReadCount, gnWriteCount, gnCompareCount))
