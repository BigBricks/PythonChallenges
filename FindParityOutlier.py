def find_outlier(integers):
    odd = []
    even = []
    for x in integers:
        if x % 2 == 0:
            even.append(x)
        else:
            odd.append(x)
    if len(odd) > len(even):
        return even[0]
    else:
        return odd[0]

