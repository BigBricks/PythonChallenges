def unique_in_order(iterable):
    arr = []
    stringI = [j for j in iterable]
    if len(iterable) == 1:
        arr.append(iterable[0])
    for n in range(len(stringI)):
        if stringI[n] != stringI[n - 1]:
            arr.append(stringI[n])
    if len(iterable) > 1 and arr == []:
        arr.append(stringI[0])
    return arr
