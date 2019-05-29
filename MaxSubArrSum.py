def maxSequence(arr):
    j = 0
    max = 0
    for x in range(0, len(arr)):
        j = j + arr[x]
        if j > max:
          max = j
        if j < 0:
          j = 0
    return max