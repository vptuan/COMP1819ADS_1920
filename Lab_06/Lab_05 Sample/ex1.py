import time
def bubbleSort(arr):
    n = len(arr)

    # Traverse through all array elements
    swapFlag = False
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n-i-1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapFlag = True

        if (swapFlag == False):
            break


if __name__ == "__main__":
    # Driver code to test above

    tests = [
        [64, 34, 25, 12, 22, 11, 90, 10, 12, 15, 100, 12, 10, 150000, 2, 5],
        [1, 3, 10, 18],
        [1, 10, 9, 20, 13]
    ]

    for i in range(0, len(tests)):
        test = tests[i]
        t1 = time.time()
        bubbleSort(test)
        t2 = time.time()
        print("TEST", i, test)
        print("TEST", i, "took", t2 - t1, "seconds to finish.")
