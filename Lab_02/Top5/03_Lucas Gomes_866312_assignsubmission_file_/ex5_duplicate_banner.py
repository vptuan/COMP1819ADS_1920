import time
def get_duplicate_banner():
    with open("./lucky_ids4.txt", "r") as file:
        student_ids = file.read().splitlines()
        checked_numbers = {} #  A Dictionary is faster than using a List, because we can check via a Key instead of iterating through list.
        duplicated_numbers = []
        for student_id in student_ids:
            if str(student_id) in checked_numbers:
                duplicated_numbers.append(student_id)

            checked_numbers[str(student_id)] = True
        return duplicated_numbers

if __name__ == "__main__":
    start_time = time.time()

    duplicated_banners = get_duplicate_banner()
    for banner in duplicated_banners:
        print(banner, end=" ")
    end_time = time.time()

    print("\nRunning time: ", end_time-start_time)
        
