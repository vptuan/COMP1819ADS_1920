def staircase(n):
    for i in range(1, n + 1):
        space_part = " " * (n-i)
        hash_part = "#" * i
        print(space_part + hash_part)


staircase(4)
staircase(15)