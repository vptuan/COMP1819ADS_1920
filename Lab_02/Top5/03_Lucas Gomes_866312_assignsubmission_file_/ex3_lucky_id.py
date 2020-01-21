def lucky_draw():
    with open("./student_ids.txt", "r") as file:
        userInput = input("What is your ID: ")
        studentIds = file.read().splitlines()
        for studentId in studentIds:
            if studentId == userInput:
                print("Yes")
                return
        print("No")
        return

if __name__ == "__main__":
    lucky_draw()