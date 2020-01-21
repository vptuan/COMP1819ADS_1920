def minmax(*args):
    return min(args), max(args)

def minmax1(*args):
    max = args[0]
    min = max
    for arg in args:
        if arg > max:
            max = arg
        if arg < min:
            min = arg
    return min, max


print(minmax(1,7,10,3,19,-2))
print(minmax1(1,7,10,3,19,-2))