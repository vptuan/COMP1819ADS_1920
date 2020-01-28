import math
import time

def isPrime(n):
    if (n % 2 == 0):
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


#r = (7772777, 111181111, 99999199999,67280421310721,311111111111113,9999999900000001)
r = (1,311111111111113)
for i in r:
    start = time.time()
    print(isPrime(i))
    end = time.time()
    print("n = {}; time = {}".format(i, end-start))