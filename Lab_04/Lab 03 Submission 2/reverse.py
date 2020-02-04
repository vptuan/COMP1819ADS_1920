from array_stack_common import ArrayStack
import time

if __name__ == "__main__":
    start_time = time.time()

    number_array = ArrayStack()
    reversed_array = ArrayStack()

    number_array.push(1)
    number_array.push(2)
    number_array.push(3)

    print("Original array:", number_array._data)

    for item in range(len(number_array._data)):
        reversed_array.push(number_array.pop())

    print("Reversed array", reversed_array._data)

    end_time = time.time()

    print("Time to calculate: ", end_time-start_time, "seconds")