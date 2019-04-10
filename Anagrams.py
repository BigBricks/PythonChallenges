from itertools import permutations as free


def anagrams(word, words):
    # your code here
    strings = [x for x in word]
    perm = free(strings)
    arr = []
    for x in perm:
        arr.append("".join(x))
    arr = set(arr)
    result = [x for x in words if x in arr]
    return result
