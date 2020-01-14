def minmax(data):
    small = big = data[0] # assuming nonempty
    for val in data:
        if val < small:
            small = val
        if val > big:
            big = val
    return small,big
