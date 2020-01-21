
# Mahid Miah - 001063915

# ------------ PROBLEM 1 ------------
def minMax(data):

    smallestNumber = data[0]
    largestNumber = data[0]

    for x in data:
        if x >= largestNumber:
            largestNumber = x
        if x <= smallestNumber:
            smallestNumber = x

    return smallestNumber, largestNumber


print(minMax((1, 2, 3, 4)))

# ------------ PROBLEM 2 ------------
def staircase(data):

    current = 0

    if data > 0 and data <= 20:
        while current <= data: # While the 'current' counter variable is less or equal to the input value 'data' the loop will continue to execute
            print('#' * current) # This line will print the hash symbol by the current value of the 'current' counter
            current = current + 1 # This increment will ensure on each line a different number of hash symbols will be printed and will also casue the loop to end when it is equal to 'data'

staircase(10)

# ------------ PROBLEM 2 version 2 ------------ This version prints staircase same way shown in the pdf
def staircase2(data):

    current = 0

    if data > 0 and data <= 20:
        while current <= data: # While the 'current' counter variable is less or equal to the input value 'data' the loop will continue to execute
            difference = data - current
            print(" " * difference + "#" * current) # This line will print the hash symbol by the current value of the 'current' counter
            current = current + 1 # This increment will ensure on each line a different number of hash symbols will be printed and will also casue the loop to end when it is equal to 'data'



staircase2(4)

# ------------ PROBLEM 3 ------------
def luckyBanner(data):
    file = open('banners.txt', 'r') # Opens the text file

    banners = [] # I will store the items from the file in this empty list

    # This for loop just adds each file line/value into the 'banners' list
    for i in file:
        banners.append(i.rstrip()) # I was using rstrip to try get rid of the '/n' in each line from the text file

    #This if/elif statement checks if the inputed 'data' value exists within the banners list
    if(data in banners):
        print('yes')
    else:
        print('no')

luckyBanner('001019441')

# ------------ PROBLEM 4 ------------
def topThree():
    file = open('banners.txt', 'r') # Opens the text file

    banners = [] # I will store the items from the file in this empty list

    # This for loop just adds each file line/value into the 'banners' list
    for i in file:
        banners.append(i.rstrip()) # I was using rstrip to try get rid of the '/n' in each line from the text file

    banners.sort() # I first numerically sorted the list
    banners.sort(reverse=True) # I then sorted it in reverse so that I can display the top 3

    # to display the top three I had then used 'len' function to get the length of the banners list (20) and then to display the top 3 I had to display 19, 18 and 17 (0-19) so for each print statement i had used the index value of the length of banners -1, -2, -3
    print(banners[len(banners) - 1])
    print(banners[len(banners) - 2])
    print(banners[len(banners) - 3])

topThree()


# ------------ PROBLEM 5 ------------
def detectdDups():
    file = open('banners.txt', 'r') # Opens the text file

    banners = [] # I will store the items from the file in this empty list
    duplicates = [] # I will store the duplicates here

    # This for loop just adds each file line/value into the 'banners' list
    for i in file:
        banners.append(i)

    # This loop is executed for each item within the 'banners' list
    for x in banners:
        # The below line counts how many times the current item in the 'for' loop (x) is counted within the banners list
        occurrences = banners.count(x)

        # If the occurrences of 'x' is more then 1 it means there is a duplicate and adds the item 'x' to the duplicates list
        if occurrences > 1:
            duplicates.append(x)

    #This line displays all the duplicates, if there is no duplicates an empty line will be displayed
    print(duplicates)


detectdDups()