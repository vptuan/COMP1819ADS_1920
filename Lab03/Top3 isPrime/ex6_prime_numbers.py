import sys
import time
def is_prime_number(num):
    """
    Time complexity is O(Sqr(n)), because the number of iterations goes up to Square of n
    """
    if num == 0 or num == 1:
        return False
    
    if num == 2:
        return True
    
    if num % 2 == 0:
        return False


    max_range = num ** 0.5
    counter = 3
    while (counter <= max_range):
        if num % counter == 0 and counter != 1:
            return False
        counter += 2
    return True


if __name__ == "__main__":
    num = 0
    if len(sys.argv) < 2:
        #num = int(input("Please insert a number: "))
        #r = (7772777, 111181111, 99999199999,67280421310721,311111111111113,9999999900000001)
        num = 311111111111113
    else:
        num = int(sys.argv[1])        
    t1 = time.time()
    print(is_prime_number(num))
    
    t2 = time.time()
    print("The algorithm took", str(t2 - t1), "seconds to complete.")

    