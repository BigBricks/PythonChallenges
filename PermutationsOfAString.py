from itertools import permutations as free


def permutations(strings):
    # your code here
    if len(strings) == 1:
        return [strings]
    perm = free(strings)
    arr = []
    for x in perm:
        arr.append("".join(x))
    arr = set(arr)
    return arr
