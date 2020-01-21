# Lucas Gomes
import time

def get_max(number_list, dict_max_exceptions):
    """
    Get the maximum value of a List


    :param number_list: List of numbers
    :param dict_max_exceptions: A dictionary composed of numbers that should be skipped. Those numbers should be the keys of this `Dict`
    """
    if len(number_list) == 0:
        return None

    max_number = None
    for number in number_list:
        if str(number) not in dict_max_exceptions and (max_number == None or number > max_number):
            max_number = number
    return max_number


def get_tops(top_number):
    with open("./lucky_ids2.txt", "r") as file:
        student_ids = file.read().splitlines()

        # store the max numbers that have been checked.
        # In theory it should be faster than using a List, because we check via a Key, instead of iterating through list.
        max_numbers_checked = {}

        for t in range(top_number): # Without reordering the list, one way is to iterate the list 'n' times to have the top `n`
            max_number = get_max(student_ids, max_numbers_checked)
            if (max_number != None):
                max_numbers_checked[str(max_number)] = True
            
        
        for max_numbers in max_numbers_checked.keys():
            print(max_numbers, end=" ")

            
        

if __name__ == "__main__":
    start_time = time.time()
    get_tops(3)
    end_time = time.time()

    print("\nRunning time: ", end_time-start_time)