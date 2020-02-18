#Bubble sort#ascending
import time
def bubbleSort(arr):
	n = len(arr)

	# Traverse through all array elements
	for i in range(n):

		# Last i elements are already in place
		for j in range(0, n-i-1):

			# traverse the array from 0 to n-i-1
			# Swap if the element found is greater
			# than the next element
			if arr[j] > arr[j+1] :
				arr[j], arr[j+1] = arr[j+1], arr[j]

# Driver code to test above
#arr = [64, 34, 25, 12, 22, 11, 90]
num = 1000
arr = []
for i in range(num):
    arr.append(i)
print(arr)

bubbleSort(arr)
start_time = time.time()
print ("Sorted array is:")
for i in range(len(arr)):
	print ("%d" %arr[i]),
end_time = time.time()
print("\nRunning time: ", end_time-start_time)
