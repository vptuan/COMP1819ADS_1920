from array_stack_common import ArrayStack

if __name__ == "__main__":
    washing_up = ArrayStack()
    drying_up = ArrayStack()

    # Add items to stack that need to be washed up
    washing_up.push("Plate")
    washing_up.push("Bowl")
    washing_up.push("Cup")
    washing_up.push("Spoon")

    print("Items left to wash: ")
    for item in washing_up._data:
        print(washing_up._data.index(item) + 1, item)
    print()

    # Once each item has been washed, add it to a stack of items to be dried
    for item in range(len(washing_up._data)):
        drying_up.push(washing_up.pop())

    for item in drying_up._data:
        print("Washed", item)

    print()

    print("Items left to dry:")
    for item in drying_up._data:
        print(drying_up._data.index(item) + 1, item)



